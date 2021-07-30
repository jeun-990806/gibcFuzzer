import random


def getData():
    return bytearray(10), 10


def randCh():
    if random.randint(0, 1) == 1:
        return random.randint(0, 255)
    special = '!*\'();:@&=+$,/?%#[]012Az-`~.\xff\x00'
    return ord(random.choice(special))


def eraseBytes(data, size):
    if size <= 1:
        return 0
    n = random.randint(1, int(size / 2))
    idx = random.randint(0, size - n)
    del data[idx:idx+n]
    return data, size - n


def insertBytes(data, size, maxSize):
    if size >= maxSize:
        return 0
    idx = random.randint(0, size)
    data.insert(idx, randCh())
    return data, size + 1


def insertRepeatedBytes(data, size, maxSize):
    kMinBytesToInsert = 3
    if size + kMinBytesToInsert >= maxSize:
        return 0

    maxBytesToInsert = min([maxSize - size, 128])
    n = random.randint(kMinBytesToInsert, maxBytesToInsert - kMinBytesToInsert)
    idx = random.randint(0, size)
    byte = random.choice([random.randint(0, 255), 0, 255])
    for i in range(0, n):
        data.insert(idx, byte)
    return data, size + n


def changeBytes(data, size, maxSize):
    if size > maxSize:
        return 0

    idx = random.randint(0, size - 2)
    data[idx] = randCh()
    return data, size


def changeBit(data, size, maxSize):
    if size > maxSize:
        return 0

    idx = random.randint(0, size - 1)
    data[idx] ^= 1 << random.randint(0, 7)
    return data, size


def shuffleBytes(data, size, maxSize):
    if size > maxSize or size == 0:
        return 0
    shuffleAmount = random.randint(1, min([size, 8]))
    shuffleStart = random.randint(0, size - shuffleAmount - 1)
    shuffled = []
    for i in range(shuffleAmount):
        shuffled.append(data[shuffleStart + 1])
        del data[shuffleStart + 1]
    random.shuffle(shuffled)
    for i in range(shuffleAmount):
        data.insert(shuffleStart, shuffled[i])
    return data, size


#구현해
def changeASCIIInteger(data, size, maxSize):
    if size > maxSize:
        return 0

    b = random.randint(0, size - 1)
    while b < size and not '''data[b]가 digit인지 확인''':
        b += 1
    if b == size:
        return 0
    e = b
    while e < size and '''data[e]가 digit인지 확인''':
        e += 1
    val = data[b] - '0'
    for i in range(b + 1, e):
        val = val * 10 + data[i] - 48

    val = random.choice([val + 1, val - 1, val / 2, val * 2, random.randint(0, val * val - 1)])
    for i in range(b, e):
        idx = e + b - i - 1
        data[idx] = val % 10 + 48
        val /= 10
    return data, size   #구현


def changeBinaryInteger(data, size):
    '''  if (Size < sizeof(T)) return 0;
  size_t Off = Rand(Size - sizeof(T) + 1);
  assert(Off + sizeof(T) <= Size);
  T Val;
  if (Off < 64 && !Rand(4)) {
    Val = Size;
    if (Rand.RandBool())
      Val = Bswap(Val);
  } else {
    memcpy(&Val, Data + Off, sizeof(Val));
    T Add = Rand(21);
    Add -= 10;
    if (Rand.RandBool())
      Val = Bswap(T(Bswap(Val) + Add)); // Add assuming different endiannes.
    else
      Val = Val + Add;               // Add assuming current endiannes.
    if (Add == 0 || Rand.RandBool()) // Maybe negate.
      Val = -Val;
  }
  memcpy(Data + Off, &Val, sizeof(Val));
  return Size;'''
    return


def copyPart():
    #
    return


def crossOver():
    #
    return


def addWordFromManualDictionary():
    #
    return


def AddWordFromPersistentAutoDictionary():
    #
    return


def test():
    maxSize = 20
    target, size = getData()
    print('empty data: ', end='')
    print(target)

    target, size = eraseBytes(target, size)
    print('erase bytes: ', end='')

    target, size = insertBytes(target, size, maxSize)
    print('insert bytes: ', end='')
    print(target)

    target, size = insertRepeatedBytes(target, size, maxSize)
    print('insert repeated bytes: ', end='')
    print(target)

    target, size = changeBytes(target, size, maxSize)
    print('change bytes: ', end='')
    print(target)

    target, size = changeBit(target, size, maxSize)
    print('change a bit: ', end='')
    print(target)

    target, size = shuffleBytes(target, size, maxSize)
    print('shuffle bytes: ', end='')
    print(target)

    # target, size = changeASCIIInteger(target, size, maxSize)
    # print('change ASCII to integer: ', end='')
    # print(target)
