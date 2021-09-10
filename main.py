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

    subprocess.call('echo %s > /sys/kernel/debug/tracing/set_ftrace_pid' % str(os.getpid()), shell=True)
    subprocess.call('echo "*sys_enter*" > /sys/kernel/debug/tracing/set_ftrace_filter', shell=True)
    subprocess.call('echo 1 > /sys/kernel/debug/tracing/events/raw_syscalls/sys_enter/enable', shell=True)
    subprocess.call('echo function > /sys/kernel/debug/tracing/current_tracer', shell=True)
    subprocess.call('echo 0 > /proc/sys/kernel/yama/ptrace_scope', shell=True)

    print('-----------------------------------\nsetting')
    print('set_ftrace_pid: ')
    subprocess.call('cat /sys/kernel/debug/tracing/set_ftrace_pid', shell=True)
    print('set_ftrace_filter: "*sys_enter*"')
    print('sys_enter: ENABLED')
    print('current_tracer: function')
    print('-----------------------------------')

    time.sleep(1)

    fuzzer = fuzzer.Fuzzer(targetFile)
    # tracer set

    if not os.path.isdir('result/' + targetName):
        print(' * make ' + targetName + ' folder in result/ directory.')
        os.mkdir('result/' + targetName, mode=0o777)
        os.mkdir('result/' + targetName + '/input/', mode=0o777)
        os.mkdir('result/' + targetName + '/output/', mode=0o777)

    startTime = time.time()
    try:
        while time.time() - startTime < 300:
            fuzzer.executeWithMutationSequence()
    finally:
        del fuzzer
    # subprocess.call('rm %s' % targetFile, shell=True)
