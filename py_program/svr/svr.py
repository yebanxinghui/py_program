from sklearn.datasets import load_boston
boston = load_boston()
#数据说明描述
#print(boston.DESCR)

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

#标准化处理
from sklearn.preprocessing import StandardScaler
ss_X = StandardScaler()
ss_y = StandardScaler()

X_train = ss_X.fit_transform(X_train)
X_test = ss_X.transform(X_test)
y_train = ss_y.fit_transform(y_train.reshape(-1,1)) #修改1
y_test = ss_y.transform(y_test.reshape(-1,1)) #修改2

#使用三种不同的核函数配置的支持向量机回归模型进行训练
from sklearn.svm import SVR

#使用线性核函数
linear_svr = SVR(kernel = 'linear')
linear_svr.fit(X_train,y_train)
linear_svr_y = linear_svr.predict(X_test)

#使用多项式核函数
poly_svr = SVR(kernel = 'poly')
poly_svr.fit(X_train,y_train)
poly_svr_y = poly_svr.predict(X_test)

#使用径向基核函数
rbf_svr = SVR(kernel = 'rbf')
rbf_svr.fit(X_train,y_train)
rbf_svr_y = rbf_svr.predict(X_test)

from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
print('R_squared value of linear SVR is ',linear_svr.score(X_test,y_test))
print('The mean squared error of linear SVR is ',mean_squared_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(linear_svr_y)))
print('The mean absolute error of linear SVR is ',mean_absolute_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(linear_svr_y)))

print('R_squared value of poly SVR is ',poly_svr.score(X_test,y_test))
print('The mean squared error of poly SVR is ',mean_squared_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(poly_svr_y)))
print('The mean absolute error of poly SVR is ',mean_absolute_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(poly_svr_y)))

print('R_squared value of rbf SVR is ',rbf_svr.score(X_test,y_test))
print('The mean squared error of rbf SVR is ',mean_squared_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(rbf_svr_y)))
print('The mean absolute error of rbf SVR is ',mean_absolute_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(rbf_svr_y)))
