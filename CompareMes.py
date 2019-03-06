#coding=utf-8
"""
@ Version : 0.1
@ Author  : pengl
@ File    : CompareMes.py
@ Project : CompareMes
@ Create Time: 2019.02.16:45
"""
import os
from Control.FormatFile import FormatFile
from Control.CompareMesTxt import CompareMesTxt
from Control.CompareMesRes import CompareMesRes
from Control.CompareMesIO import CompareMesIO
from Control.CreateComparsionReport import CreateComparisonReport

class CompareMesObject():
    '''
    参数说明：storagePath->存放路径；targetFileName->目标文件名称；standardFileName->标准文件名称
    targetFileP2P->目标文件能否点对点，设置源文本存放路径
    standarFileP2P->标准文件点对点
    '''
    def __init__(self,storagePath,targetFileName,standardFileName):
        self.storagePath=storagePath
        self.targetFileName=targetFileName
        self.standardFileName=standardFileName

    #比对文件，并生成结果
    def CompareMes(self):
        #将当前目录切换到存放路径
        os.chdir(self.storagePath)
        #在存放路径里判断和创建临时文件夹存放中间文件
        if not os.path.exists('tmp'):
            os.mkdir('tmp')

        #分别格式化目标文件和标准文件
        targetFileP2P=FormatFile(fileName='targetFileName')
        standarFileP2P=FormatFile(fileName='standardFileName')

        #选择已格式化的文件，生成对比文件
        compareMesTxt=CompareMesTxt(targetFileP2P,standarFileP2P)

        #生成比对结果
        compareMesRes=CompareMesRes(targetFileP2P,standarFileP2P)

        # 为UI输出创建对比文本输出内容
        CompareMesIO.CompareMesIO(targetFileP2P, standarFileP2P)

        return targetFileP2P

        # 生成比对报告
        result=CreateComparisonReport(file1=targetFileP2P)
       