import pprint
import fileManagement


class CodeGenerator:
    __code = ''

    def __init__(self, functionName, argumentList, headerFileList, path='targetCodes/'):
        self.__path = path
        self.__functionName = functionName
        self.__arguments = argumentList
        self.__headerFiles = headerFileList

    def __getArgStr(self):
        result = ''
        index = 0
        for argument in self.__arguments:
            if argument == 'void':
                return ''
            if '*' not in argument:
                if '...' not in argument:
                    result += 'data[%d][0], ' % index
            else:
                result += 'data[%d], ' % index
            index += 1
        return result[:-2]

    def generate(self):
        self.__code = '//' + self.__functionName + '\n'
        for header in self.__headerFiles:
            if header != 'unistd.h' and header != 'fcntl.h' and header != 'stdint.h':
                self.__code += '#include <' + header + '>\n'
        self.__code += '#include <stdint.h>\n#include <unistd.h>\n#include <fcntl.h>\n'
        self.__code += 'char tracer[256] = \"/sys/kernel/debug/tracing/tracing_on\";\n' \
                       'char marker[256] = \"/sys/kernel/debug/tracing/trace_marker\";\n\n'
        self.__code += 'int target(uint8_t **data) {\n' \
                       '\tint trace_fd = open(tracer, O_WRONLY);\n' \
                       '\tint marker_fd = open(marker, O_WRONLY);\n' \
                       '\tif(trace_fd >= 0 && marker_fd >= 0){ \n' \
                       '\t\twrite(trace_fd, "1", 1);\n' \
                       '\t\twrite(marker_fd, "start\\n", 7);\n' \
                       '\t\t%s(%s);\n' \
                       '\t\twrite(marker_fd, "end\\n", 5);\n' \
                       '\t\twrite(trace_fd, "0", 1);\n' \
                       '\t}' % (self.__functionName, self.__getArgStr())
        self.__code += '\treturn 0;\n}'

    def getCode(self):
        return self.__code

    def exportCode(self):
        file = open(self.__path + self.__functionName + '.c', 'w')
        file.write(self.__code)
        file.close()


functionDataDict = fileManagement.openData('targetGlibc.dict')
function = 'access'
maker = CodeGenerator(function, functionDataDict[function]['arguments'],
                      functionDataDict[function]['header file'])
maker.generate()
maker.exportCode()
