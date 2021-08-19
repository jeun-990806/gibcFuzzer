import cffi
import targetFunctionScanner


class Builder:
    __ffi = cffi.FFI()
    __arguments = []
    __targetFunction = ''
    __sourceCode = ''
    __ftraceFunctions = r'''    int setTrace = -1;
                                int marker = -1;
            
                                int openFtraceFiles(void){
                                    char ftracePath[256] = "/sys/kernel/debug/tracing/tracing_on";
                                    char markerPath[256] = "/sys/kernel/debug/tracing/trace_marker";
                                    setTrace = open(ftracePath, O_WRONLY);
                                    marker = open(markerPath, O_WRONLY);
                                    return (setTrace > 0) && (marker > 0);
                                }
            
                                void ftraceStart(void){
                                    openFtraceFiles();
                                    if(setTrace != -1 && marker != -1){
                                        write(setTrace, "1", 1);
                                        write(marker, "start_ftrace", 13);
                                    }else{
                                        printf("cannot open ftrace files.\n");
                                    }
                                }
                                void ftraceStop(void){
                                    if(setTrace != -1 && marker != -1){
                                        write(marker, "stop_ftrace", 12);
                                        write(setTrace, "0", 1);
                                        close(marker);
                                        close(setTrace);
                                    }else{
                                        printf("cannot open ftrace files.\n");
                                    }
                                }'''

    def __init__(self, srcPath, functionName):
        self.__arguments = targetFunctionScanner.TargetFunctionScanner(srcPath, functionName).getArguments()
        self.__setTargetFunction()
        self.__generateSourceCode(srcPath, functionName)

    def __setTargetFunction(self):
        self.__targetFunction = 'void target('
        for argument in self.__arguments:
            self.__targetFunction += '%s %s, ' % (argument[0], argument[1])
        self.__targetFunction = self.__targetFunction[:-2] + ')'

    def __generateSourceCode(self, originPath, functionName):
        originFile = open(originPath, 'r')
        originCode = ''.join(originFile.readlines())
        if '<unistd.h>' not in originCode:
            originCode = '#include <unistd.h>\n' + originCode
        if '<fcntl.h>' not in originCode:
            originCode = '#include <fcntl.h>\n' + originCode
        targetCode = '\n%s{\n' \
                     '\tftraceStart();' \
                     '\t%s(' % (self.__targetFunction, functionName)
        for argument in self.__arguments:
            targetCode += argument[1] + ', '
        targetCode = targetCode[:-2] + ');'
        targetCode += '\tftraceStop();' \
                      '\n};'
        self.__sourceCode = originCode + self.__ftraceFunctions + targetCode

    def __setSourceCode(self):
        self.__ffi.cdef(self.__targetFunction + ';')
        self.__ffi.set_source('target', self.__sourceCode)

    def build(self):
        self.__setSourceCode()
        self.__ffi.compile(verbose=False)
