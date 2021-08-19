import re
import importlib
import cffi

import byteMutator


class Fuzzer:
    __ffi = cffi.FFI()

    __mutators = []

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
        newInput = self.__makeMutationSequence()
        self.__targetFunction.target(*newInput)
        traceLog = open('/sys/kernel/debug/tracing/trace', 'r')
        return newInput, self.__getSyscallSet(traceLog.readlines())

    def __getSyscallSet(self, traceLog):
        syscallSet = []
        logging = False
        for line in traceLog:
            if 'mark_write:' in line:
                logging = True ^ logging
            if logging and 'sys_enter' in line:
                syscallSet.append(line[line.find('NR ') + 3:line.rfind(' (')])
        return syscallSet
