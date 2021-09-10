import random


class ByteMutator:
    def __init__(self, minLength=4, maxLength=4):
        self.__maxLength = maxLength
        self.__minLength = minLength
        self.__currentMutation = bytearray(minLength)
        self.__length = minLength
        self.__mutationNum = 0

    def getMutation(self):
        self.__mutationNum += 1
        op = random.randint(1, 6)
        if op == 1:
            self.__eraseBytes()
        elif op == 2:
            self.__insertBytes()
        elif op == 3:
            self.__changeBytes()
        elif op == 4:
            self.__changeBit()
        elif op == 5:
            self.__shuffleBytes()
        elif op == 6:
            self.__changeToASCII()
        return self.__currentMutation

    # noinspection PyMethodMayBeStatic
    def __randCh(self):
        if random.randint(0, 1) == 1:
            return random.randint(97, 123)  #
        special = '!*\'();:@&=+$,/?%#[]012Az-`~.\xff\x00'
        return ord(random.choice(special))

    def __eraseBytes(self):
        if self.__length > self.__minLength:
            del self.__currentMutation[random.randint(0, self.__length - 1)]
            self.__length -= 1

    def __insertBytes(self):
        if self.__length < self.__maxLength:
            self.__currentMutation.insert(random.randint(0, self.__length - 1), self.__randCh())
            self.__length += 1

    def __changeBytes(self):
        self.__currentMutation[random.randint(0, self.__length - 1)] = self.__randCh()

    def __changeBit(self):
        self.__currentMutation[random.randint(0, self.__length - 1)] ^= 1 << random.randint(0, 7)

    def __shuffleBytes(self):
        if self.__length > 1:
            start = random.randint(0, self.__length - 2)
            end = random.randint(start + 1, self.__length - 1)
            head = self.__currentMutation[:start]
            shuffledPart = self.__currentMutation[start:end]
            random.shuffle(shuffledPart)
            tail = self.__currentMutation[end:]
            self.__currentMutation = head + shuffledPart + tail

    def __changeToASCII(self):
        for i in range(len(self.__currentMutation)):
            if self.__currentMutation[i] < 32:
                self.__currentMutation[i] = 32
            if self.__currentMutation[i] > 126:
                self.__currentMutation[i] = 126
