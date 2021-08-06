import fileManagement
import os

sourceFilePath = 'structure_list/'
destinationPath = 'structure_proto_files/'


def getStructListFileList(path=None):
    global sourceFilePath
    if path is not None and os.path.isdir(path):
        sourceFilePath = path
    return os.listdir(sourceFilePath)


def readListFileContent(fileName, path=None):
    global sourceFilePath
    if path is not None and os.path.isdir(path):
        sourceFilePath = path
    file = fileManagement.openData(sourceFilePath + fileName)
    return file


def convertTypeToProtobufType(fieldType, fieldName):
    converted = ''
    if '[' in fieldName:
        converted = 'repeated '
    if 'unsigned' in fieldType:
        return converted + 'int32'
    elif fieldType == 'int' or fieldType == 'char' or fieldType == 'short' or fieldType == 'long' or fieldType == 'short int' or fieldType == 'long int':
        return converted + 'sint32'
    elif fieldType == 'uint8_t' or fieldType == 'uint16_t' or fieldType == 'uint32_t':
        return converted + 'uint32'
    elif fieldType == 'uint64_t':
        return converted + 'uint64'
    elif 'char' in fieldType and '*' in fieldType:
        if fieldType.count('*') == 2:
            return 'repeated string'
        return converted + 'string'
    elif '*' in fieldType:
        return converted + 'int32'


for elem in getStructListFileList():
    if len(readListFileContent(elem)) != 0:
        print(elem)
        print('origin:', end=' ')
        print(readListFileContent(elem))
        print([convertTypeToProtobufType(dataType.strip().replace('  ', ' '), name) for dataType, name in readListFileContent(elem)])
