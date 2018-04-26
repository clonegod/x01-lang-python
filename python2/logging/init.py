import os
import sys

workdir  = r"E:\tmp\pytest"

def addModulePath():
    os.chdir(workdir )
    sys.path.append(workdir )
    print 'Successfully add %s to module search path' % workdir 

addModulePath()