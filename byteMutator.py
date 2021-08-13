import defaultMutator
import random


class ByteMutator(defaultMutator.DefaultMutator):
    def __init__(self, maxLength=4):
        super().__init__()
        self.__maxLength = maxLength
        self.__newMutation = bytearray(maxLength)

    def getByteMutation(self):
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
        return self.__newMutation

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
            n = random.randint(kMinBytesToInsert, maxBytesToInsert - kMinBytesToInsert)
            idx = random.randint(0, length)
            byte = random.choice([random.randint(0, 255), 0, 255])
            for i in range(0, n):
                self.__newMutation.insert(idx, byte)

    def __changeBytes(self):
        length = len(self.__newMutation)
        if length <= self.__maxLength:
            idx = random.randint(0, length - 1)
            self.__newMutation[idx] = self.__randCh()

    def __changeBit(self):
        length = len(self.__newMutation)
        if length <= self.__maxLength:
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
