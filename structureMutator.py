import random

import defaultMutator
import byteMutator
import importlib
import ctypes
import sys

import fileManagement


class StructureMutator(defaultMutator.DefaultMutator):
    __structureListFilePath = ''
    __structureName = ''

    __structure = None
    __field = []

    __insideMutators = []

    def __init__(self, structureName, listFilePath=None, protobufFilePath=None):
        super().__init__()
        if listFilePath is not None:
            self.__structureListFilePath = listFilePath
        self.__structureName = structureName
        self.__field = fileManagement.openData(listFilePath + structureName + '.list')
        sys.path.insert(1, protobufFilePath)  # 다른 폴더에 존재하는 .py files(.proto 파일의 컴파일 결과)를 import하기 위함
        for field in self.__field:
            maxLength = self.__numberOfBytes(field[0])
            self.__insideMutators.append(byteMutator.ByteMutator(maxLength))

    # noinspection PyMethodMayBeStatic
    def __numberOfBytes(self, fieldType):
        if fieldType == 'int':
            return 4
        elif fieldType == 'char':
            return 1

    def getMutation(self):
        protobuf = importlib.import_module(self.__structureName + '_pb2')
        self.__structure = protobuf.Structure()
        idx = 0
        for field in self.__field:
            mutation = self.__insideMutators[idx].getMutation()
            if field[0] == 'int' or field[0] == 'char':
                mutation = int.from_bytes(mutation, byteorder='big', signed=True)
            setattr(self.__structure, field[1], mutation)
            idx += 1

    def printStructures(self):
        print(self.__structureName)
        for field in self.__field:
            print(field[1], end=': ')
            print(getattr(self.__structure, field[1]))
