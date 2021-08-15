import os
import ctypes
import struct

import defaultMutator
import random


class ByteMutator(defaultMutator.DefaultMutator):
    __absolutePath = os.path.abspath(__file__)[:os.path.abspath(__file__).rfind('/')]
    __maxLength = 0

    def __init__(self, dataType, signed=True):
        super().__init__()
        self.__dataType = dataType
        self.__signed = signed
        self.__maxLength = self.__getNBytes(dataType)
        self.__newMutation = bytearray(self.__maxLength)

    # noinspection PyMethodMayBeStatic
    def __getNBytes(self, dataType):
        bytesWithType = {1: ['char'],
                         2: ['short'],
                         4: ['int', 'float'],
                         8: ['long long', 'double', 'long double']}
        # long type은 운영체제에 따라 크기가 다르기 때문에 별도의 계산이 필요하다.
        byteSizeCalculator = ctypes.CDLL(self.__absolutePath + '/util/byteSizeCalculator.so')
        bytesWithType[byteSizeCalculator.longTypeBytes()].append('long')

        for byte in bytesWithType.keys():
            if dataType in bytesWithType[byte]:
                return byte
        # str 자료형의 max byte를 100으로 설정 (이 부분 잘 수정해 볼 것.)
        return 100

    def getMutation(self):
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
        if self.__dataType == 'int' or self.__dataType == 'long' or self.__dataType == 'short'\
                or self.__dataType == 'long long' or self.__dataType == 'char':
            return int.from_bytes(self.__newMutation, byteorder='big', signed=self.__signed)
        elif self.__dataType == 'str':
            return ctypes.create_string_buffer(bytes(self.__newMutation), self.__maxLength + 1)
        elif self.__dataType == 'float':
            return struct.unpack('f', self.__newMutation)[0]

    # noinspection PyMethodMayBeStatic
    def __randCh(self):
        if random.randint(0, 1) == 1:
            return random.randint(0, 255)
        special = '!*\'();:@&=+$,/?%#[]012Az-`~.\xff\x00'
        return ord(random.choice(special))

    def __eraseBytes(self):
        length = len(self.__newMutation)
        if length > 1:
            eraseAmount = random.randint(1, int(length / 2))
            idx = random.randint(0, int(length - eraseAmount))
            del self.__newMutation[idx:idx + eraseAmount]

    def __insertBytes(self):
        while len(self.__newMutation) < self.__maxLength and random.randint(0, 1) == 1:
            idx = random.randint(0, len(self.__newMutation))
            self.__newMutation.insert(idx, self.__randCh())

    def __insertRepeatedBytes(self):
        length = len(self.__newMutation)
        kMinBytesToInsert = 3
        if length + kMinBytesToInsert < self.__maxLength:
            maxBytesToInsert = min([self.__maxLength - length, 128])
            n = random.randint(kMinBytesToInsert, maxBytesToInsert + 1)
            idx = random.randint(0, length)
            byte = random.choice([random.randint(0, 255), 0, 255])
            for i in range(0, n):
                self.__newMutation.insert(idx, byte)

    def __changeBytes(self):
        length = len(self.__newMutation)
        if 0 < length <= self.__maxLength:
            if length == 1:
                idx = 0
            else:
                idx = random.randint(0, length - 1)
            self.__newMutation[idx] = self.__randCh()

    def __changeBit(self):
        length = len(self.__newMutation)
        if 0 < length <= self.__maxLength:
            if length == 1:
                idx = 0
            else:
                idx = random.randint(0, length - 1)
            self.__newMutation[idx] ^= 1 << random.randint(0, 7)

    def __shuffleBytes(self):
        length = len(self.__newMutation)
        if self.__maxLength >= length > 0:
            startIdx = random.randint(0, length - 1)
            endIdx = random.randint(startIdx + 1, length + 1)
            shuffled = self.__newMutation[startIdx:endIdx]
            tail = self.__newMutation[endIdx:]
            random.shuffle(shuffled)
            self.__newMutation[startIdx:] = shuffled + tail
