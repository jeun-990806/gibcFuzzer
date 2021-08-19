import sys
import os

import fuzzer
import targetCodeBuilder
import targetFunctionScanner


if len(sys.argv) > 2:
    path = sys.argv[1]
    targetName = sys.argv[2]
    targetFile = None
    if os.path.isfile(path):
        targetFile = path
    else:
        raise NameError('no such file. (' + path + ')')
    fileName = targetFile[targetFile.rfind('/') + 1:targetFile.rfind('.')]

    propertyFileGenerator = targetFunctionScanner.TargetFunctionScanner(targetFile, targetName)
    propertyFilePath = propertyFileGenerator.exportToPropertyFile()
    codeGenerator = targetCodeBuilder.Builder(path, targetName)
    codeGenerator.build()

    fuzzer = fuzzer.Fuzzer(targetFile)
    syscallSet = set()
    for i in range(1000):
        executionResult = fuzzer.executeWithMutationSequence()
        newSyscallSet = set(executionResult[1])
        if len(newSyscallSet - syscallSet) != 0:
            print('%dth execution:' % i)
            print(executionResult[0])
            print(newSyscallSet)
            syscallSet = syscallSet | newSyscallSet

    del fuzzer
