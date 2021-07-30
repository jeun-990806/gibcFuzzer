import pprint

import fileManagement as fm
import random


targetArgType = ['int', 'char', 'size_t', 'int *', 'char *', 'void', '...']


def getType(arg):
    if arg == 'void' or arg == '...':
        return arg
    arg = arg.replace('restrict ', '').replace('const ', '')
    argType = arg[:arg.rfind(' ')]
    if '*' in arg:
        argType += ' *'
    return argType


def checkArg(argList):
    for arg in argList:
        if getType(arg) not in targetArgType:
            return False
    return True


def getTargetFunctionWithArgs(data):
    result = []
    for function in data.keys():
        if checkArg(data[function][0]['arguments']):
            result.append(function)
    return result


def generate(headers, function, arguments):
    headerDecl = ''
    for header in headers:
        headerDecl += '#include <' + header + '>\n'
    targetFunction = '#include <stdint.h>\nint target(uint8_t **data){\n' \
                     '\t%s(%s);\n' \
                     '\treturn 0;\n' \
                     '}' % (function, convertArgsToStr(arguments))
    targetInfoFunction = 'char *targetInfo(void){' \
                         ' return \"%s\";' \
                         '}' % function
    return headerDecl + targetFunction + '\n' + targetInfoFunction


def convertArgsToStr(arguments):
    result = ''
    index = 0
    for argument in arguments:
        if argument == 'void':
            return ''
        if '*' not in argument:
            result += 'data[%d][0], ' % index
        else:
            result += 'data[%d], ' % index
        index += 1
    return result[:-2]


glibc = fm.openData('targetGlibc.dict')

sampleFunction = random.choice(list(glibc.keys()))
print(sampleFunction)
code = generate(glibc[sampleFunction][0]['header file'], sampleFunction, glibc[sampleFunction][0]['arguments'])
f = open('target.c', 'w')
f.write(code)
f.close()
