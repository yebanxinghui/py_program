#k近邻算法实现
from numpy import *
import operator
#operator是运算符模块

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

#kNN算法具体实现,其中有四个输入参数
#用于分类的输入向量inX，输入的训练样本集为dataSet,标签向量为labels，用于选择最近邻的数目为k
#其中的距离度量为欧几里得距离
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0] #数据集的行数
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    #对于二维数组,axis=1表示按行相加 , axis=0表示按列相加
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    #X.argsort()将X中的元素从小到大排序，提取其对应的index（索引）并输出,但X本身的次序没变动
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse=True)
    #operator.itemgetter(1)为定义了一个取第一个域值的函数
    return sortedClassCount[0][0]

group,labels=createDataSet()
classify0([0,0],group,labels,3)

#使用knn算法改进约会网站的配对效果(???)
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)#文件行数
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat,classLabelVector

datingDataMat,datingLabels = file2matrix('E:\PythonPackage\MLiA_SourceCode\machinelearninginaction\Ch02\datingTestSet2.txt')
'''
该数据集有三列数据和一列特征标记
第一列为每年获得的飞行常客数据
第二列为玩游戏视频所耗时间公分比
第三列为每周消费的冰淇淋公升数
第三列为特征标记，有不喜欢，魅力一般和极具魅力三种
'''

#使用散点图分析
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()

#归一化特征
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals-minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges, minVals

normMat,ranges,minVals = autoNorm(datingDataMat)
print(normMat)
print(ranges)
print(minVals)

#测试评估错误率
def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix('E:\PythonPackage\MLiA_SourceCode\machinelearninginaction\Ch02\datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("the classifier came back with: %d, the real answer is : %d" %(classifierResult,datingLabels[i]))
        if(classifierResult != datingLabels[i]):
            errorCount += 1.0
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))

datingClassTest()

#用户输入预测
def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix('E:\PythonPackage\MLiA_SourceCode\machinelearninginaction\Ch02\datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print("You will probably like this person: " , resultList[classifierResult-1])

classifyPerson()

#将图像转化为向量,将32x32的二进制图像矩阵转化为1x1024的向量
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

testVector = img2vector("E:/PythonPackage/MLiA_SourceCode/machinelearninginaction/Ch02/digits/trainingDigits/0_13.txt")

import os
def handwritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir('E:/PythonPackage/MLiA_SourceCode/machinelearninginaction/Ch02/digits/trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector("E:/PythonPackage/MLiA_SourceCode/machinelearninginaction/Ch02/digits/trainingDigits/%s" % fileNameStr)
    testFileList = os.listdir('E:/PythonPackage/MLiA_SourceCode/machinelearninginaction/Ch02/digits/testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('E:/PythonPackage/MLiA_SourceCode/machinelearninginaction/Ch02/digits/testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)
        print("The classifier came back with: %d, the real answer is: %d" %(classifierResult,classNumStr))
        if(classifierResult != classNumStr):
            errorCount+=1.0
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount/float(mTest)))

handwritingClassTest()