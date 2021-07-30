import fileManagement as fm
import random


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
        result += 'data[%d], ' % index
        index += 1
    return result[:-2]


def test():
    glibc = fm.openData('glibc.dict')

    sampleFunction = 'printf'
    print(sampleFunction)
    print(glibc[sampleFunction][0]['arguments'])
    code = generate(glibc[sampleFunction][0]['header file'], sampleFunction, glibc[sampleFunction][0]['arguments'])
    f = open('target.c', 'w')
    f.write(code)
    f.close()
