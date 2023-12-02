import os
from os.path import os as path

DIR_CURRENT = os.getcwd()

def GetPath(dir):
    dir_raiz = path.abspath(path.join(DIR_CURRENT, os.pardir))
    return (path.join(dir_raiz,dir))


