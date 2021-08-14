import ctypes

import defaultMutator
import random


class ByteMutator(defaultMutator.DefaultMutator):
    __maxLength = 0

    def __init__(self, dataType='byte', signed=True):
        super().__init__()
        self.__dataType = dataType
        self.__signed = signed
        self.__maxLength = 4
        if dataType == 'str':
            self.__maxLength = 30
        self.__newMutation = bytearray(self.__maxLength)

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
        if self.__dataType == 'byte':
            return bytes(self.__newMutation)
        elif self.__dataType == 'str':
            return ctypes.create_string_buffer(bytes(self.__newMutation), self.__maxLength + 1)

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
