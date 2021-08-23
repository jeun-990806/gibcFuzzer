import re


class TargetFunctionScanner:
    def __init__(self, srcPath, functionName):
        self.__sourceFilePath = srcPath
        self.__targetFunctionName = functionName
        self.__sourceCode = self.__getFileContent()
        self.__functionDeclaration = self.__getPartOfFunction(self.__getFunctionDeclarationLine(), part=0)

    def __getFileContent(self):
        file = open(self.__sourceFilePath, 'r')
        content = file.readlines()
        file.close()
        return content

    # 함수 선언이 이루어진 라인을 탐색하여 반환
    def __getFunctionDeclarationLine(self):
        for line in self.__sourceCode:
            if self.__targetFunctionName in line and '(' in line:
                return line
        print('TargetFunctionScanner: no target function ' + self.__targetFunctionName +
              ', (' + self.__sourceFilePath + ')')

    # 문자열(=함수 선언문)을 받아 각 부분으로 나누어 반환
    # (return type:1) (function name) ((arguments:2)) (entire function:0)
    # noinspection PyMethodMayBeStatic
    def __getPartOfFunction(self, declaration=None, part=2):
        if declaration is None:
            declaration = self.__functionDeclaration
        basicFunctionRE = '([a-zA-Z_][a-zA-Z0-9_\s]*[a-zA-Z0-9_](?:\s[*]+|[*]*))\s?' \
                          + self.__targetFunctionName + \
                          '\(([a-zA-Z0-9_\s,*]*)\)'
        if declaration is not None:
            return re.search(basicFunctionRE, declaration).group(part)

    def getArguments(self):
        argumentRE = '([a-zA-Z_][a-zA-Z0-9_\s]*[a-zA-Z0-9_][*]*)\s([*]*[a-zA-Z_][a-zA-Z0-9_]*)'
        if self.__functionDeclaration is not None:
            argumentsStr = self.__getPartOfFunction(self.__functionDeclaration.replace('restrict ', ''), 2)
            if argumentsStr == 'void':
                return []
            arguments = re.findall(argumentRE, argumentsStr)
            argumentsConv = []
            for argType, argName in arguments:              # 띄어쓰기에 따라 asterisk가 매개변수 이름에 붙어 있을 수도 있음.
                for i in range(argName.count('*')):         # 매개변수 이름으로 들어간 asterisk를 매개변수 타입 부분으로 옮겨준다.
                    argType += '*'
                argName = argName.replace('*', '')
                argumentsConv.append((argType, argName))
            return argumentsConv

    def getHeaderFiles(self):
        includeRE = '#(?:include|INCLUDE)[\s]<([a-zA-Z0-9][a-zA-Z0-9_/]+\.h)>'
        headerFiles = re.findall(includeRE, ''.join(self.__sourceCode))
        return headerFiles

    def getReturnType(self):
        return self.__getPartOfFunction(part=1)

    def __propertiesToStr(self):
        properties = 'NAME=%s;\nRETURN_TYPE=%s;\n' % (self.__targetFunctionName, self.getReturnType())
        properties += 'HEADER_FILES=%s;\n' % ' '.join(self.getHeaderFiles())
        idx = 1
        for arg in self.getArguments():
            properties += 'ARG%d=%s;\n' % (idx, arg[0])
            idx += 1
        return properties

    def exportToPropertyFile(self):
        propertyFilePath = 'properties/'
        propertyFileName = self.__sourceFilePath[self.__sourceFilePath.rfind('/') + 1:self.__sourceFilePath.rfind('.')]\
                           + '.pro'
        propertyFile = open(propertyFilePath + propertyFileName, 'w')
        propertyFile.write(self.__propertiesToStr())
        propertyFile.close()
        return propertyFilePath + propertyFileName
