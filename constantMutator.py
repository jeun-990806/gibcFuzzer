import random
import fileManagement


class ConstantMutator:
    __symbolicConstantsPath = ''
    __headerFiles = []
    symbolicConstantsList = []

    __usedSymbolicConstants = []

    def __init__(self, headerFileNameList, path='.'):
        self.__symbolicConstantsPath = path
        for header in headerFileNameList:
            self.symbolicConstantsList += fileManagement.openData(path + header + '.list')

    def getASymbolicConstants(self):
        symbolicConstant = random.choice(self.symbolicConstantsList)
        self.__usedSymbolicConstants.append(symbolicConstant)
        return symbolicConstant
