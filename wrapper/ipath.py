# -*- coding:UTF-8 -*-
#ipath

import os,os.path
import shutil

#拷贝目录【类似unix下的cp -r aa bb】
def copyDir(srcDir,dstDir):
    if os.path.exists(srcDir):
        __copyDir(srcDir,dstDir)
    else:
        print(srcDir+' not exist')

def __copyDir(srcDir,dstDir):
    if not os.path.exists(dstDir):
        shutil.copytree(srcDir,dstDir)
        return
    lists=os.listdir(srcDir)
    for lt in lists:
        srcPath=os.path.join(srcDir,lt)
        goalPath=os.path.join(dstDir,lt)
        if os.path.isfile(srcPath):
            shutil.copyfile(srcPath,goalPath)
        else:
            __copyDir(srcPath,goalPath)

#拷贝目录下指定类型文件【类似unix下的cp aa/*.xx bb】
def copyDirExtFiles(srcDir,dstDir,ext,recursion=False):
    if os.path.exists(srcDir):
        __copyDirExtFiles(srcDir,dstDir,ext,recursion)
    else:
        print(srcDir+' not exist')

def __copyDirExtFiles(srcDir,dstDir,ext,recursion=False):
    if not os.path.exists(dstDir):
        os.mkdir(dstDir)
    lists=os.listdir(srcDir)
    for lt in lists:
        srcPath=os.path.join(srcDir,lt)
        goalPath=os.path.join(dstDir,lt)
        if os.path.isfile(srcPath):
            tu=os.path.splitext(srcPath)
            if tu[1]==ext:
                shutil.copyfile(srcPath,goalPath)
        elif recursion==True :
            __copyDirExtFiles(srcPath,goalPath,ext,recursion)

#删除文件夹下指定类型文件【类型unix下的 rm aa/*.xx】
def delExtFiles(srcDir,ext,recursion=False):
    lists=os.listdir(srcDir)
    for lt in lists:
        srcPath=os.path.join(srcDir,lt)
        if os.path.isfile(srcPath):
            tu=os.path.splitext(lt)
            if tu[1]==ext:
                os.remove(srcPath)
        elif recursion==True:
            delExtFiles(srcPath,ext,recursion)

#删除文件夹下所有文件【类似unix下的 rm -r aa/bb】
def rmDirAllFiles(dstDir):
    lists=os.listdir(dstDir)
    for lt in lists:
        srcPath=os.path.join(dstDir,lt)
        if os.path.isfile(srcPath):
            os.remove(srcPath)
        else:
            shutil.rmtree(srcPath)

#复制文件
def copyFile(srcFile,dstFile):
    if os.path.isfile(srcFile):
        shutil.copyfile(srcFile,dstFile)

#复制文件到指定目录【类似unix下 cp .xx bb】
def copyFileToDir(srcFile,dstDir):
    if os.path.isfile(srcFile):
        tu=os.path.split(srcFile)
        copyFile(srcFile,os.path.join(dstDir,tu[1]))

#删除文件【类似unix下 rm aa.xx】
def rmFile(fullPath):
    if os.path.isfile(fullPath):
        os.remove(fullPath)

#删除文件夹【类似unix下 rm -r aa】
def rmFloder(dstDir):
    if os.path.exists(dstDir):
        shutil.rmtree(dstDir)




