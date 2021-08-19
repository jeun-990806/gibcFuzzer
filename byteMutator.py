import copy
import cffi
import struct

import defaultMutator
import random


class ByteMutator(defaultMutator.DefaultMutator):
    __ffi = cffi.FFI()

    def __init__(self, varType='int', maxLength=4):
        super().__init__()
        self.__maxLength = maxLength
        self.__varType = varType
        self.__currentMutation = bytearray(maxLength)

    def getMutation(self):
        while True:
            exMutation = copy.deepcopy(self.__currentMutation)
            op = random.randint(0, 6)
            if op == 0:
                self.__eraseBytes()
            elif op == 1:
                self.__insertBytes()
            elif op == 2:
                self.__insertRepeatedBytes()
            elif op == 3:
                self.__changeBytes()
            elif op == 4:
                self.__changeBit()
            elif op == 5:
                self.__shuffleBytes()
            elif op == 6:
                self.__changeToASCII()
            if exMutation != self.__currentMutation and 0 < len(self.__currentMutation) < self.__maxLength:
                break

        if self.__varType == 'float' or self.__varType == 'double':
            return self.__ffi.cast(self.__varType, random.uniform(-100, 100))
        if self.__varType == 'char*':
            return self.__ffi.new('char []', bytes(self.__currentMutation))
        return self.__ffi.cast(self.__varType, int.from_bytes(self.__currentMutation, byteorder='big'))

    # noinspection PyMethodMayBeStatic
    def __randCh(self):
        if random.randint(0, 1) == 1:
            return random.randint(97, 123)  #
        special = '!*\'();:@&=+$,/?%#[]012Az-`~.\xff\x00'
        return ord(random.choice(special))

    def __eraseBytes(self):
        length = len(self.__currentMutation)
        if length > 1:
            eraseAmount = random.randint(1, int(length / 2))
            idx = random.randint(0, int(length - eraseAmount))
            del self.__currentMutation[idx:idx + eraseAmount]

    def __insertBytes(self):
        while len(self.__currentMutation) < self.__maxLength and random.randint(0, 1) == 1:
            idx = random.randint(0, len(self.__currentMutation))
            self.__currentMutation.insert(idx, self.__randCh())

    def __insertRepeatedBytes(self):
        length = len(self.__currentMutation)
        kMinBytesToInsert = 3
        if length + kMinBytesToInsert < self.__maxLength:
            maxBytesToInsert = min([self.__maxLength - length, 128])
            n = random.randint(kMinBytesToInsert, maxBytesToInsert + 1)
            idx = random.randint(0, length)
            byte = self.__randCh()  #
            for i in range(0, n):
                self.__currentMutation.insert(idx, byte)

    def __changeBytes(self):
        length = len(self.__currentMutation)
        if 0 < length <= self.__maxLength:
            if length == 1:
                idx = 0
            else:
                idx = random.randint(0, length - 1)
            self.__currentMutation[idx] = self.__randCh()

    def __changeBit(self):
        length = len(self.__currentMutation)
        if 0 < length <= self.__maxLength:
            if length == 1:
                idx = 0
            else:
                idx = random.randint(0, length - 1)
            self.__currentMutation[idx] ^= 1 << random.randint(0, 7)

    def __shuffleBytes(self):
        length = len(self.__currentMutation)
        if self.__maxLength >= length > 0:
            startIdx = random.randint(0, length - 1)
            endIdx = random.randint(startIdx + 1, length + 1)
            shuffled = self.__currentMutation[startIdx:endIdx]
            tail = self.__currentMutation[endIdx:]
            random.shuffle(shuffled)
            self.__currentMutation[startIdx:] = shuffled + tail

    def __changeToASCII(self):
        for i in range(len(self.__currentMutation)):
            if self.__currentMutation[i] < 32:
                self.__currentMutation[i] = 32
            if self.__currentMutation[i] > 126:
                self.__currentMutation[i] = 126

    def resetMutation(self):
        self.__currentMutation = bytearray(1)
