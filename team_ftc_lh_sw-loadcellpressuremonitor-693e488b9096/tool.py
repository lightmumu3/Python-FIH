import os
import os.path
# UI文件所在的路径
dir='./'

#列出目录下的所有UI文件
def listUiFile():
    list = []
    files = os.listdir(dir)
    for filename in files:
        # print(dir+os.sep+f)
        # print(filename)
        if os.path.splitext(filename)[1] == '.ui':
            list.append(filename)

    return list

def listQrcFile():
    list = []
    files = os.listdir(dir)
    for filename in files:
        # print(dir+os.sep+f)
        # print(filename)
        if os.path.splitext(filename)[1] == '.qrc':
            list.append(filename)
    return list


# 把扩展名为.ui的文件改成扩展名为.py的文件

def transPyFile(filename):
    return os.path.splitext(filename)[0] + '.py'

def transQrcPyFile(filename):
    return os.path.splitext(filename)[0] + '_rc.py'

# 调用系统命令把UI文件转换成Python文件

def runMain():
    list = listUiFile()
    for uifile in list:
        pyfile = transPyFile(uifile)
        cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile,uifile=uifile)
        #print(cmd)
        os.system(cmd)

def runQrc():
    list = listQrcFile()
    for qrcfile in list:
        pyfile = transQrcPyFile(qrcfile)
        cmd = 'pyrcc5 -o {pyfile} {qrcfile}'.format(pyfile=pyfile,qrcfile=qrcfile)
        #print(cmd)
        os.system(cmd)

######程序的主入口

if __name__ == "__main__":
    runMain()
    runQrc()
