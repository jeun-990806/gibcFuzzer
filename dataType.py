import cffi
import byteMutator
import structureMutator


class DataType:
    __ffi = cffi.FFI()
    __dataTypeDict = {'int': ['char', 'short', 'int', 'long', 'long  long'
                              'signed', 'unsigned',
                              'signed char', 'unsigned char', 'signed short', 'unsigned short',
                              'signed int', 'unsigned int', 'signed long', 'unsigned long',
                              'signed long long', 'unsigned long long'],
                      'floating-point': ['float', 'double', 'long double'],
                      'string': ['char*']}

    def __init__(self, typeName):
        self.__name = typeName

    def getMutator(self):
        category = self.getCategory()
        if category == 'string':
            return byteMutator.ByteMutator(1, 50)
        elif category == 'structure':
            return structureMutator.StructureMutator(self.__name)
        else:
            return byteMutator.ByteMutator(self.__ffi.sizeof(self.__name), self.__ffi.sizeof(self.__name))

    def getCategory(self):
        formalDataType = self.makeFormalDataType()
        for category in self.__dataTypeDict.keys():
            if formalDataType in self.__dataTypeDict[category]:
                return category
        return 'structure'

    def makeFormalDataType(self):
        otherKeywords = ['restrict', 'const']
        formalDataType = self.__name
        for keyword in otherKeywords:
            formalDataType = formalDataType.replace(keyword, '')
        return formalDataType.strip()