import ctypes
from ctypes import *
import fileManagement as fm
import random
import secrets

shared_lib = '/home/jeun/PycharmProjects/test/target.so'
target = CDLL(shared_lib)

target.targetInfo.restype = ctypes.c_char_p
target.target.argtypes = (ctypes.Array, )
# returnVal = target.targetInfo()


def makeInputList(size):
    return (ctypes.POINTER(ctypes.c_uint8) * size)()


def mutateInputList(inputList, size):
    for i in range(len(inputList)):
        inputList[i] = ctypes.cast(secrets.token_bytes(size), ctypes.POINTER(ctypes.c_uint8))


def getFunctionName():
    return target.targetInfo().decode('utf-8')


def getArgumentList(functionName):
    glibc = fm.openData('glibc.dict')
    return glibc[functionName][0]['arguments']


def convertArgListToArgTypeList(arguments):
    result = []
    return result


inputSize = 1  # 만들 input의 개수
outputs = []
while 1:
    inputs = makeInputList(inputSize)
    mutateInputList(inputs, 10)
    result = target.target(inputs)
    if result == -1:
        break

print(outputs)
