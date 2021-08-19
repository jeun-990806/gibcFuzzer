import fileManagement
import re

glibc = fileManagement.openData('glibc_data/targetGlibc.dict')
for function in glibc.keys():
    headerDeclaration = ['#include <' + header + '>' for header in glibc[function]['header file']]
    headerDefine = '\n'.join(headerDeclaration)
    glibcDefine = '%s %s(%s);' % (glibc[function]['return type'], function, ', '.join(glibc[function]['arguments']))
    glibcDefine = glibcDefine.replace('* ', '*')
    targetFile = open('target_codes/' + function + '.c', 'w')
    targetFile.write(headerDefine + '\n\n' + glibcDefine)
    targetFile.close()