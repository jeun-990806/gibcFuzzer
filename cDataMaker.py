import struct
import cffi
import dataType


class CDataMaker:
    __ffi = cffi.FFI()

    def __checkIsSigned(self, dataType):
        if 'unsigned' in dataType or dataType == 'char':
            return False
        return True

    def castToCDataType(self, byteSequence, dataTypeName):
        dataType = dataType.DataType(dataTypeName)
        category = dataType.getCategory()
        if category == 'int':
            return self.__ffi.cast(dataType.makeFormalDataType(),
                                   int.from_bytes(byteSequence, byteorder='big',
                                                  signed=self.__checkIsSigned(dataTypeName)))
        elif category == 'floating-point':
            return self.__ffi.cast(dataType.makeFormalDataType(), struct.unpack(dataTypeName[0], byteSequence)[0])
        elif category == 'string':
            return self.__ffi.new('char []', bytes(byteSequence))
        elif '*' in dataTypeName:
            value = self.castToCDataType(byteSequence, dataTypeName[:-1])
            return self.__ffi.new(dataType.makeFormalDataType(), value)
        raise NameError(dataTypeName + 'is not basic C Data Type.')


def cmakerTestCode():
    ffi = cffi.FFI()
    data = [('int', int.to_bytes(22, byteorder='big', length=4)),
            ('const char*', b'hello world\n'),
            ('float*', bytes(struct.pack("f", 3.14))),
            ('int*', int.to_bytes(85, byteorder='big', length=4))]
    cDataList = []
    maker = CDataMaker()
    for elem in data:
        cDataList.append(maker.castToCDataType(elem[1], elem[0]))
    print(ffi.string(cDataList[1], 13))
    print(ffi.unpack(cDataList[-2], 1))
    print(ffi.unpack(cDataList[-1], 1)) # 마지막 int *형 변수가 가리키는 곳에 값이 잘 들어갔는지 확인
    print(ffi.sizeof('float'))