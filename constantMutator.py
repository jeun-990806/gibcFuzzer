import ctypes

import defaultMutator
import random
import fileManagement


class ConstantMutator(defaultMutator.DefaultMutator):
    __symbolicConstantsPath = ''
    __headerFiles = []
    symbolicConstantsList = []

    def __init__(self, headerFileNameList, path='.'):
        super().__init__()
        self.__symbolicConstantsPath = path
        for header in headerFileNameList:
            self.symbolicConstantsList += fileManagement.openData(path + header + '.list')

    def getMutation(self):
        symbolicConstant = random.choice(self.symbolicConstantsList)
        # self.__usedInputList.append(symbolicConstant)
        return symbolicConstant
