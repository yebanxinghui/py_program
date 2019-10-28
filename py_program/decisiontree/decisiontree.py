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

#采用单一回归树模型
from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor()
dtr.fit(X_train,y_train)
dtr_y = dtr.predict(X_test)

from sklearn.ensemble import RandomForestRegressor,ExtraTreesRegressor,GradientBoostingRegressor
#采用随机森林模型
rfr = RandomForestRegressor()
rfr.fit(X_train,y_train)
rfr_y = rfr.predict(X_test)

#采用极端森林模型
etr = ExtraTreesRegressor()
etr.fit(X_train,y_train)
etr_y = etr.predict(X_test)

#采用梯度提升模型
gbr = GradientBoostingRegressor()
gbr.fit(X_train,y_train)
gbr_y = gbr.predict(X_test)

#对单一回归树做出预测
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
print('R_squared value of DecisionTreeRegressor is ',dtr.score(X_test,y_test))
print('The mean squared error of DecisionTreeRegressor is ',mean_squared_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(dtr_y)))
print('The mean absolute error of DecisionTreeRegressor is ',mean_absolute_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(dtr_y)))

#对随机森林做出预测
print('R_squared value of RandomForestRegressor is ',rfr.score(X_test,y_test))
print('The mean squared error of RandomForestRegressor is ',mean_squared_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(rfr_y)))
print('The mean absolute error of RandomForestRegressor is ',mean_absolute_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(rfr_y)))

#对极端森林做出预测
print('R_squared value of ExtraTreesRegressor is ',etr.score(X_test,y_test))
print('The mean squared error of ExtraTreesRegressor is ',mean_squared_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(etr_y)))
print('The mean absolute error of ExtraTreesRegressor is ',mean_absolute_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(etr_y)))
#输出每种特征的贡献度
print(np.sort(list(zip(etr.feature_importances_,boston.feature_names)),axis = 0))

#对梯度提升做出预测
print('R_squared value of GradientBoostingRegressor is ',gbr.score(X_test,y_test))
print('The mean squared error of GradientBoostingRegressor is ',mean_squared_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(gbr_y)))
print('The mean absolute error of GradientBoostingRegressor is ',mean_absolute_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(gbr_y)))

