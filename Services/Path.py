import os
import platform

DIR_CURRENT = os.getcwd()

def GetPath(arq):
    return (DIR_CURRENT+formatPath(GetOs(),"audio",arq))

def GetOs():
    return platform.system()

def formatPath(os,path,arq):
    return '\\{}\\{}'.format(path,arq) if GetOs() == "Windows" else '/{}/{}'.format(path,arq)