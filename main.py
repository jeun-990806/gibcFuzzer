import random
import sys
import os
import subprocess

import glibcFuzzer


def converter(fileName):
    f = open(fileName, 'r')
    outputs = []
    record = False
    fileContents = f.readlines()
    for line in fileContents:
        if 'start' in line:
            outputs.append(line)
            record = True
        if record:
            if 'sys_enter' in line:
                outputs.append(line)
        if 'end' in line:
            outputs.append(line)
            break
    outf = open(fileName[:fileName.rfind('.')] + '_converted.txt', 'w')
    outf.writelines(outputs)
    outf.writelines(fileContents[-3:-1])
    f.close()
    outf.close()
    return outputs


def getArgType(argument):  # arg: [argType] [argName] 에서 [argType] 반환
    argType = argument[:argument.rfind(' ')] + ' '
    argName = argument[argument.rfind(' ') + 1:]
    for i in range(argName.count('*')):
        argType += '*'
    return argType.strip()


def checkArgs(argument):  # argument type 체크해서 fuzzing 가능 여부를 반환
    availableKeywords = {'const', '*restrict', 'signed', '..'}
    availableTypes = {'int', 'char', 'void', 'short', 'long', 'float', 'double', 'size_t'}
    argumentTypes = set(getArgType(argument).split(' '))
    unmatchedTypes = argumentTypes - availableKeywords - availableTypes
    if '(' in argument or ')' in argument:
        return False
    if len(unmatchedTypes) == 0 or unmatchedTypes == {'*'}:
        return True
    return False


if len(sys.argv) > 1:
    path = sys.argv[1]
    targetFile = None
    subprocess.call('echo 1 > /sys/kernel/debug/tracing/events/raw_syscalls/sys_enter/enable', shell=True)
    if path.endswith('/'):
        if os.path.isdir(path):
            targetFile = os.listdir(path)
        else:
            print('main.py: no such directory.')
    else:
        if os.path.isfile(path):
            targetFile = path
        else:
            print('main.py: no such file.')

    if type(targetFile) is list:
        file = random.choice(targetFile)
        subprocess.call('cc -fPIC -shared -o %s %s' %
                        ('sharedLibs/' + file[:file.rfind('.')] + '.so', path + file), shell=True)
        print(file)
        fuzzer = glibcFuzzer.Fuzzer('targetCodes/' + file)
        for i in range(30):
            mutation = fuzzer.fuzzing()
            subprocess.call('cat /sys/kernel/debug/tracing/trace >> tracing_result.txt', shell=True)
            print(mutation)
        del fuzzer

    elif targetFile is not None:
        subprocess.call('cc -fPIC -shared -o %s %s' %
                        ('sharedLibs' + targetFile[targetFile.rfind('/'):targetFile.rfind('.')] + '.so', targetFile),
                        shell=True)
        fuzzer = glibcFuzzer.Fuzzer(targetFile)
        for i in range(30):
            mutation = fuzzer.fuzzing()
            subprocess.call('cat /sys/kernel/debug/tracing/trace >> tracing_result.txt', shell=True)
            print(mutation)
        del fuzzer
