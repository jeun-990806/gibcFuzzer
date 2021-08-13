import fileManagement
import os
import subprocess

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
    converted = 'optional '
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


fieldInfo = fileManagement.openData('structure_list/struct_test.list')
fileContent = 'syntax = \"proto2\";\npackage glibcFuzzer;\n\nmessage Structure {\n\t'
idx = 1

for fieldType, fieldName in fieldInfo:
    fileContent += convertTypeToProtobufType(fieldType, fieldName) + ' ' + fieldName + ' = %d;\n\t' % idx
    idx += 1

fileContent += '}'
newProtoFile = open('structure_proto_files/struct_test.proto', 'w')
newProtoFile.write(fileContent)
newProtoFile.close()
subprocess.call('protoc -I=structure_proto_files --python_out=. structure_proto_files/struct_test.proto', shell=True)
