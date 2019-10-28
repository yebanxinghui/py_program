#决策树
from math import log
import operator
#计算信息熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

def createDataSet():
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels

myDat,labels = createDataSet()
print(myDat)
print(calcShannonEnt(myDat))
myDat[0][-1] = 'maybe'
print(myDat)
print(calcShannonEnt(myDat))

#划分数据集，三个参数分别是：待划分的数据集，划分数据集的特征，需要返回的特征的值
def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for featVec in dataSet:
        if(featVec[axis] == value):
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

myDat,labels = createDataSet()
print(myDat)
splitDataSet(dataSet,0,1)
splitDataSet(dataSet,0,0)

#选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0])-1 #特征的数量，目前是2
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy #基尼系数，也就是信息增益
        if(infoGain>bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

myDat,labels = createDataSet()
chooseBestFeatureToSplit(myDat)

#计算出现次数最多的分类名称
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0;
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]

#构建决策树函数
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree

myDat,labels = createDataSet()
mytree = createTree(myDat,labels)
print(mytree)

import matplotlib.pyplot as plt
decisionNode = dict(boxstyle = 'sawtooth',fc = '0.8')
#使用dict(a="a",b="b")返回字典形式的数据类型{"a":"a","b":"b"}
leafNode = dict(boxstyle = 'round4',fc = '0.8')
arrow_args = dict(arrowstyle = '<-')
'''
annotate()图形增加注释
https://blog.csdn.net/qq_30638831/article/details/79938967
https://blog.csdn.net/TeFuirnever/article/details/88946088
'''
#nodeText为显示的文本，centerPt为箭头所在的点，parentPt为指向文本的初始点
def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(nodeTxt,xy = parentPt,xycoords = 'axes fraction',\
    xytext = centerPt,textcoords = 'axes fraction',va='center',ha='center',bbox=nodeType,\
    arrowprops=arrow_args)

from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] 
'''
产生中文乱码的原因就是字体的默认设置中并没有中文字体，
所以我们只要手动添加中文字体的名称就可以了
'''
def createPlot():
    fig = plt.figure(1,facecolor='white')
    fig.clf()#清除所有轴，但是窗口打开，这样它可以被重复使用
    createPlot.ax1 = plt.subplot(111,frameon=True)#frameon为是否显示边框，creatplot.ax1为全局变量
    plotNode(U'决策结点',(0.5,0.1),(0.1,0.5),decisionNode)
    plotNode(U'叶节点',(0.8,0.1),(0.3,0.8),leafNode)
    plt.show()
createPlot()

#获取叶节点的数目和树的层数
def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if(type(secondDict[key])).__name__=='dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs

def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            thisDepth = 1+getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth>maxDepth:
            maxDepth = thisDepth
    return maxDepth
    
def retrieveTree(i):
    listOfTrees = [{'no surfacing':{0:'no',1:{'flippers':{0:'no',1:'yes'}}}},\
                   {'no surfacing':{0:'no',1:{'flippers':{0:{'head':{0:'no',1:'yes'}},1:'no'}}}}]
    return listOfTrees[i]
print(retrieveTree(1))
myTree = retrieveTree(0)
getNumLeafs(myTree)
getTreeDepth(myTree)


#在父子节点间填充文本信息
def plotMidText(cntrPt,parentPt,txtString):
    xMid=(parentPt[0]-cntrPt[0])/2.0+cntrPt[0]
    yMid=(parentPt[0]-cntrPt[0])/2.0+cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)
