# import the packets
import numpy as np
import pandas as pd

DATA_PATH = "E:/py_program/breast-cancer/breast-cancer-wisconsin.data"
#创建特征列表
columnNames = [
    'Sample code number',
    'Clump Thickness',
    'Uniformity of Cell Size',
    'Uniformity of Cell Shape',
    'Marginal Adhesion',
    'Single Epithelial Cell Size',
    'Bare Nuclei',
    'Bland Chromatin',
    'Normal Nucleoli',
    'Mitoses',
    'Class'
]

#貌似这里可以直接从互联网直接下载指定数据
#data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer/breast-cancer-wisconsin.data',names=columnNames)
data = pd.read_csv(DATA_PATH, names = columnNames)

#显示数据大小(显示的是两个元素的元组，分别为行数和列数)
print(data.shape)
#缺失值处理，暂时先将？替换为标准缺失值Nan
data = data.replace(to_replace = "?", value = np.nan)
#丢弃带有标准缺失值的数据(dropna函数丢弃的指定为Nan值)
data = data.dropna(how = 'any')
print(data.shape)

#分割数据集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    data[ columnNames[1:10] ], #特征值
    data[ columnNames[10]   ], #标记值
    test_size = 0.25, #因为一般采用25%的数据作为测试集，剩下75%的用于构建训练集合
    random_state = 33
)

'''
X_train ： 训练数据集的特征
X_test ：  测试数据集的特征
y_train ： 训练数据集的标签
y_test ：  测试数据集的标签
'''

#查验训练样本的数量和类别分布
#y_train.value_counts()
'''
2    344 
4    168
Name: Class, dtype: int64
训练样本一共512条数据，其中344条良性肿瘤数据，168条恶性肿瘤数据
'''
#查验测试样本的数量和类别分布
#y_train.value_counts()
'''
2    100
4     71
Name: Class, dtype: int64
测试样本一共171条数据，其中100条良性肿瘤数据，71条恶性肿瘤数据
'''

#应用机器模型前，应该将数据标准化
#即保证每个特征的数值转化为均值为0，方差为1的数据(其实就是归一化，使数据位于-1~1之间)，使训练出的模型不会被某些维度过大的值主导。
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train = ss.fit_transform(X_train) # fit_transform for train data
X_test = ss.transform(X_test)

#建立三个机器学习模型
#这里我们选用逻辑斯蒂回归模型
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_y = lr.predict(X_test)

#这里我们选择支持向量机回归svm模型
from sklearn.svm import LinearSVC
lsvc = LinearSVC()
lsvc.fit(X_train, y_train)
svm_y = lsvc.predict(X_test)

#这里我们选择随机梯度下降模型(参数估计)的方法
from sklearn.linear_model import SGDClassifier
sgdc = SGDClassifier()
sgdc.fit(X_train,y_train)
sgdc_y = sgdc.predict(X_test)

#分类器的效果评估,这里我们着重关注召回率，即 正阳性/(正阳性+假阴性)
from sklearn.metrics import classification_report
#先查看逻辑斯蒂回归的精确性
print('Accuracy of the LogesticRegression: ', lr.score(X_test, y_test))
print(classification_report(y_test, lr_y, target_names = ['Benign', 'Malignant']))
#查看svm的精确性
print('Accuracy of the svm: ', lsvc.score(X_test, y_test))
print(classification_report(y_test, svm_y, target_names = ['Benign', 'Malignant']))
#最后查看随机梯度下降模型的精确性
print('Accuracy of the SGD: ' , sgdc.score(X_test, y_test))
print(classification_report(y_test, sgdc_y, target_names = ['Benign', 'Malignant']))

