import pandas as pd
titanic = pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')
#分离数据特征与预测目标
y = titanic['survived']
X = titanic.drop(['row.names','name','survived'],axis = 1)

#对缺失数据进行填充
X['age'].fillna(X['age'].mean(),inplace = True)
X.fillna('UNKNOWN',inplace = True)

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, #特征值
    y, #标记值
    test_size = 0.25, #因为一般采用25%的数据作为测试集，剩下75%的用于构建训练集合
    random_state = 33
)

#类别型特征向量化
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()
X_train = vec.fit_transform(X_train.to_dict(orient = 'record'))
X_test = vec.transform(X_test.to_dict(orient = 'record'))

#输出处理后特征向量的维度
print(len(vec.feature_names_))

#使用决策树模型依靠所有特征进行预测，并做性能评估
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(X_train,y_train)
print(dt.score(X_test,y_test))

#导入特征筛选器
from sklearn import feature_selection
#筛选出前20%的特征，使用相同配置的决策树模型进行预测，并且评估性能
fs = feature_selection.SelectPercentile(feature_selection.chi2,percentile = 20)
X_train_fs = fs.fit_transform(X_train,y_train)
dt.fit(X_train_fs,y_train)
X_test_fs = fs.transform(X_test)
print(dt.score(X_test_fs,y_test))

#通过交叉验证的方法，按照固定间隔的百分比筛选特征，并作图展示性能随特征筛选比例的变化
from sklearn.cross_validation import cross_val_score
import numpy as np
percentiles = range(1,100,2)
results = []

for i in percentiles:
    fs = feature_selection.SelectPercentile(feature_selection.chi2,percentile = i)
    X_train_fs = fs.fit_transform(X_train,y_train)
    scores = cross_val_score(dt,X_train_fs,y_train,cv=5)
    results = np.append(results,scores.mean())
print(results)

opt = np.where(results == results.max())[0][0]
print('Option number of feature %d ' % percentiles[opt])

import pylab as pl
pl.plot(percentiles,results)
pl.xlabel('percentiles of features')
pl.ylabel('accuracy')
pl.show()

#使用最佳删选后的特征，利用相同配置的模型在测试集上进行性能评估
fs = feature_selection.SelectPercentile(feature_selection.chi2,percentile = 7)
X_train_fs = fs.fit_transform(X_train,y_train)
dt.fit(X_train_fs,y_train)
X_test_fs = fs.transform(X_test)
print(dt.score(X_test_fs,y_test))
