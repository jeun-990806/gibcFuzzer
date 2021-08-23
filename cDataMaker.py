import struct
import cffi


class CDataMaker:
    __ffi = cffi.FFI()
    __dataTypeDict = {'int': ['char', 'short', 'int', 'long'],
                      'floating-point': ['float', 'double', 'long double'],
                      'pointer': ['short*', 'int*', 'long*', 'float*', 'double*', 'long double*'],
                      'string': ['char*']}

    def __replaceKeywords(self, dataType):
        return dataType.replace('const', '').replace('restrict', '').strip()

    def __printErrorMessage(self, message):
        raise NameError(message)

    def __getDataTypeCategory(self, dataType):
        for key in self.__dataTypeDict.keys():
            if dataType in self.__dataTypeDict[key]:
                return key
        self.__printErrorMessage(dataType + 'is not supported.')

    def __checkIsSigned(self, dataType):
        if 'unsigned' in dataType or dataType == 'char':
            return False
        return True

    def castToCDataType(self, byteSequence, dataType):
        dataType = self.__replaceKeywords(dataType)
        category = self.__getDataTypeCategory(dataType)
        if category == 'int':
            return self.__ffi.cast(dataType,
                                   int.from_bytes(byteSequence, byteorder='big', signed=self.__checkIsSigned(dataType)))
        elif category == 'floating-point':
            return self.__ffi.cast(dataType, struct.unpack(dataType[0], byteSequence)[0])
        elif category == 'pointer':
            value = self.castToCDataType(byteSequence, dataType.replace('*', ''))
            return self.__ffi.new(dataType, value)
        elif category == 'string':
            return self.__ffi.new('char []', bytes(byteSequence))


def cmakerTestCode():
    ffi = cffi.FFI()
    data = [('int', int.to_bytes(22, byteorder='big', length=4)),
            ('char*', b'hello world\n'),
            ('float*', bytes(struct.pack("f", 3.14))),
            ('int*', int.to_bytes(85, byteorder='big', length=4))]
    cDataList = []
    maker = CDataMaker()
    for elem in data:
        cDataList.append(maker.castToCDataType(elem[1], elem[0]))
    print(ffi.unpack(cDataList[-2], 1))
    print(ffi.unpack(cDataList[-1], 1)) # 마지막 int *형 변수가 가리키는 곳에 값이 잘 들어갔는지 확인
