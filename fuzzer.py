import os
import re
import importlib
import cffi

import byteMutator


class Fuzzer:
    __ffi = cffi.FFI()
    __mutators = []
    __foundedSyscallSet = set()
    __inputSyscallsTable = []
    __pid = str(os.getpid())

    __executionNum = 0

    def __init__(self, path):
        self.__targetCodePath = path
        targetFileName = path[path.rfind('/') + 1:path.rfind('.')]
        self.__properties = ''.join(open('properties/' + targetFileName + '.pro', 'r').readlines())
        self.__targetFunctionArguments = self.__getArguments()
        self.__setMutators()
        self.__targetFunction = importlib.import_module('target').lib

    def __getArguments(self):
        argumentRE = '^ARG[1-9][0-9]*=([^;]*);'
        return re.findall(argumentRE, self.__properties, re.MULTILINE)

    def __setMutators(self):
        for arg in self.__targetFunctionArguments:
            if arg != 'char *':
                newMutator = byteMutator.ByteMutator(arg, self.__ffi.sizeof(arg))
            else:
                newMutator = byteMutator.ByteMutator(arg, 500)
            self.__mutators.append(newMutator)

    def __makeMutationSequence(self):
        return [mutator.getMutation() for mutator in self.__mutators]

    def executeWithMutationSequence(self):
        self.__executionNum += 1
        newInput = self.__makeMutationSequence()
        self.__targetFunction.target(*newInput)
        syscallSet = self.__getSyscallSet()
        if self.__checkNewSyscall(syscallSet):
            self.__inputSyscallsTable.append((newInput, syscallSet))
            print('%dth execution: ' % self.__executionNum, end='')
            print(newInput, end=', ')
            print('called syscall numbers: ', end='')
            print(syscallSet)

    def __checkNewSyscall(self, newSyscalls):
        if len(newSyscalls - self.__foundedSyscallSet) != 0:
            self.__updateFoundedSyscalls(newSyscalls)
            return True
        return False

    def __getTraceLog(self):
        traceFile = open('/sys/kernel/debug/tracing/trace', 'r')
        traceLog = traceFile.readlines()
        traceFile.close()
        return traceLog

    def __getSyscallSet(self):
        traceLog = self.__getTraceLog()
        syscallSet = set()
        readOn = False
        for line in traceLog:
            if 'start_ftrace' in line:
                readOn = True
                continue
            if 'stop_ftrace' in line:
                break
            if readOn and 'sys_enter:' in line and self.__pid in line:
                syscallSet.add(line[line.find('NR ') + 3:line.rfind(' (')])
        return syscallSet

    def __updateFoundedSyscalls(self, newSyscalls):
        self.__foundedSyscallSet = self.__foundedSyscallSet | newSyscalls