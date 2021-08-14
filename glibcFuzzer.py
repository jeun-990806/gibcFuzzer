import defaultMutator
import byteMutator
import constantMutator

import fileManagement
import ctypes

import structureMutator


class Fuzzer:
    __sharedLibPath = '/home/jeun/PycharmProjects/glibcFuzzer/sharedLibs/'
    __glibcFunctionInfo = fileManagement.openData('glibc.dict')

    __mutators = []
    __usedMutation = None

    def __init__(self, path):
        self.__targetCodePath = path
        targetCodeFile = open(path, 'r')
        self.__targetFunctionName = targetCodeFile.readline()[2:-1]
        self.__targetFunctionArguments = self.__glibcFunctionInfo[self.__targetFunctionName][0]['arguments']
        self.__targetFunctionHeaders = self.__glibcFunctionInfo[self.__targetFunctionName][0]['header file']
        self.__mutators = [self.__getMutator(arg, self.__targetFunctionHeaders)
                           for arg in self.__targetFunctionArguments]
        self.__targetFunction = ctypes.CDLL(self.__sharedLibPath + self.__targetFunctionName + '.so')

    # noinspection PyMethodMayBeStatic
    def __getArgType(self, argument):  # arg: [argType] [argName]
        argType = argument[:argument.rfind(' ')] + ' '
        argName = argument[argument.rfind(' ') + 1:]
        for i in range(argName.count('*')):
            argType += '*'
        return argType.strip()

    # noinspection PyMethodMayBeStatic
    def __getMutator(self, arg, headers):
        otherKeywords = {'const', '*restrict', 'signed'}
        byteTypes = {'int', 'char', 'void', 'short', 'long', 'float', 'double', 'size_t'}
        constantKeywords = ['flag', 'mode', 'type', 'opt']

        argumentTypes = set(self.__getArgType(arg).split(' '))
        if arg == '...':
            return None
        if len(argumentTypes - otherKeywords - byteTypes) == 0 or \
                argumentTypes - otherKeywords - byteTypes == {'*'}:
            for keyword in constantKeywords:
                if keyword in arg:
                    return constantMutator.ConstantMutator(headers, 'symbolic_constants_list/')
            mutationTypes = list(argumentTypes & byteTypes)
            if 'char' in mutationTypes and '*' in arg:
                return byteMutator.ByteMutator(dataType='str')
            return byteMutator.ByteMutator(dataType='byte')
        else:
            return structureMutator.StructureMutator(self.__getArgType(arg).replace(' ', '_'))

    def __makeMutationSequence(self):
        newInputSequence = (ctypes.POINTER(ctypes.c_uint8) * (len(self.__targetFunctionArguments)))()
        newMutationSequence = []
        for i in range(len(self.__mutators)):
            if self.__mutators[i] is None:
                continue
            mutation = self.__mutators[i].getMutation()
            newMutationSequence.append(mutation)
            newInputSequence[i] = ctypes.cast(mutation, ctypes.POINTER(ctypes.c_uint8))
        return newInputSequence, newMutationSequence

    def fuzzing(self):
        newInput, newMutation = self.__makeMutationSequence()
        self.__targetFunction.target(newInput)
        self.__usedMutation = newInput
        return newMutation
