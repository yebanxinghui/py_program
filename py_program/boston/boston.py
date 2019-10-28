from sklearn.datasets import load_boston
boston = load_boston()
#数据说明描述
print(boston.DESCR)

'''
Boston House Prices dataset
===========================

Notes
------
Data Set Characteristics:  

    :Number of Instances: 506 

    :Number of Attributes: 13 numeric/categorical predictive
    
    :Median Value (attribute 14) is usually the target

    :Attribute Information (in order):
        - CRIM     per capita crime rate by town
        - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
        - INDUS    proportion of non-retail business acres per town
        - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
        - NOX      nitric oxides concentration (parts per 10 million)
        - RM       average number of rooms per dwelling
        - AGE      proportion of owner-occupied units built prior to 1940
        - DIS      weighted distances to five Boston employment centres
        - RAD      index of accessibility to radial highways
        - TAX      full-value property-tax rate per $10,000
        - PTRATIO  pupil-teacher ratio by town
        - B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
        - LSTAT    % lower status of the population
        - MEDV     Median value of owner-occupied homes in $1000's

    :Missing Attribute Values: None

    :Creator: Harrison, D. and Rubinfeld, D.L.
    一共有506条有效数据，13种特征和目标房价，没有缺失的属性或者特征值
'''

from sklearn.cross_validation import train_test_split

import numpy as np

X = boston.data
y = boston.target

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state = 33,test_size = 0.25)

print('The max target value is ',np.max(boston.target))
print('The min target value is ',np.min(boston.target))
print('The average target value is ',np.mean(boston.target))

#标准化处理
from sklearn.preprocessing import StandardScaler
ss_X = StandardScaler()
ss_y = StandardScaler()

X_train = ss_X.fit_transform(X_train)
X_test = ss_X.transform(X_test)
y_train = ss_y.fit_transform(y_train.reshape(-1,1)) #修改1
y_test = ss_y.transform(y_test.reshape(-1,1)) #修改2

#使用线性回归模型
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,y_train)
lr_y = lr.predict(X_test)

#使用随机梯度下降即SGD模型
from sklearn.linear_model import SGDRegressor
sgdr = SGDRegressor(max_iter = 5) #参数增添修改可选，否则warning
sgdr.fit(X_train,y_train.ravel()) #使用扁平化函数ravel，否则warning
shdr_y = sgdr.predict(X_test)

#LinearRegression模型自带的评估函数
print('The value of default measurement of LinearRegression is ',lr.score(X_test,y_test))

from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error

#使用r2_score模块
print('The value of R_squared of LinearRegression is ',r2_score(y_test,lr_y))

#使用mean_squared_error模块
print('The mean squared error of LinearRegression is ',mean_squared_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(lr_y)))

#使用mean_absolute_error模块
print('The mean absolute error of LinearRegression is ',mean_absolute_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(lr_y)))



