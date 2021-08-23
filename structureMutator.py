import byteMutator
import cffi
import re


class StructureMutator:
    __fields = []
    __mutation = []

    __mutators = []
    __ffi = cffi.FFI()

    def __init__(self, structureName, structureFilePath=''):
        self.__structureName = structureName
        if structureFilePath == '':
            self.__structureFilePath = 'structures/' + structureName + '.structure'
        else:
            self.__structureFilePath = structureFilePath
        with open(self.__structureFilePath, 'r') as f:
            self.__structureInfo = ''.join(f.readlines())
        self.__setFields()
        self.__setMutators()

    def __setFields(self):
        argumentRE = '^FIELD[1-9][0-9]*=([^;]*);'
        self.__fields = re.findall(argumentRE, self.__structureInfo, re.MULTILINE)

    def printFields(self):
        print(self.__fields)

    def __setMutators(self):
        for field in self.__fields:
            if field == 'float':
                newMutator = byteMutator.ByteMutator(field, 4)
            elif 'char' not in field and '*' not in field:
                newMutator = byteMutator.ByteMutator(field, self.__ffi.sizeof(field))
            else:
                newMutator = byteMutator.ByteMutator(field, 50)  # 문자열 최대 길이
            self.__mutators.append(newMutator)

    def __mutateStructrue(self):
        self.__mutation = [mutator.getMutation() for mutator in self.__mutators]

    def getMutation(self):
        self.__mutateStructrue()
        return self.__mutation