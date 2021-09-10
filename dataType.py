import random

import cffi
import byteMutator
import structureMutator


class DataType:
    __ffi = cffi.FFI()
    __dataTypeDict = {'int': ['char', 'short', 'int', 'long', 'long long', 'size_t',
                              'signed', 'unsigned',
                              'signed char', 'unsigned char', 'signed short', 'unsigned short',
                              'signed int', 'unsigned int', 'signed long', 'unsigned long',
                              'signed long long', 'unsigned long long'],
                      'floating-point': ['float', 'double', 'long double'],
                      'string': ['char*'],
                      'void-pointer': ['void*']}

    def __init__(self, typeName):
        self.name = typeName


    def getMutator(self):
        category = self.getCategory()
        if category == 'void-pointer':
            self.name = 'int*'
            size = min(self.__ffi.sizeof(self.name), 8)
            return byteMutator.ByteMutator(size, size)
        else:
            size = min(self.__ffi.sizeof(self.name), 8)
        if category == 'string':
            return byteMutator.ByteMutator(1, 50)
        elif category == 'structure':
            return structureMutator.StructureMutator(self.name)
        else:
            return byteMutator.ByteMutator(size, size)

    def getCategory(self):
        formalDataType = self.makeFormalDataType()
        for category in self.__dataTypeDict.keys():
            if formalDataType in self.__dataTypeDict[category]:
                return category
        if '*' in formalDataType:
            return 'pointer'
        return 'structure'

    def makeFormalDataType(self):
        otherKeywords = ['restrict', 'const']
        formalDataType = self.name
        for keyword in otherKeywords:
            formalDataType = formalDataType.replace(keyword, '')

        return formalDataType.strip()