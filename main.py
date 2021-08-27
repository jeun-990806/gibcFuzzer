import sys
import os
import time
import subprocess

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
    # tracer set
    subprocess.call('echo "*sys_enter*" > /sys/kernel/debug/tracing/set_ftrace_filter', shell=True)
    subprocess.call('echo "*mark_write*" >> /sys/kernel/debug/tracing/set_ftrace_filter', shell=True)
    subprocess.call('echo 1 > /sys/kernel/debug/tracing/events/raw_syscalls/sys_enter/enable', shell=True)
    subprocess.call('echo function > /sys/kernel/debug/tracing/current_tracer', shell=True)

    if not os.path.isdir('result/' + targetName):
        os.mkdir('result/' + targetName)
        os.mkdir('result/' + targetName + '/input/')
        os.mkdir('result/' + targetName + '/output/')

    startTime = time.time()
    while time.time() - startTime < 300:
        fuzzer.executeWithMutationSequence()
    del fuzzer
