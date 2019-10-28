X_train = [[6],[8],[10],[14],[18]]
y_train = [[7],[9],[13],[17.5],[18]]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

import numpy as np
#在x轴上从0到25均匀采样100个数据点
xx = np.linspace(0,25,100)
xx = xx.reshape(xx.shape[0],1)
#将上述100个数据点作为基准，预测回归直线
yy = regressor.predict(xx)

#对回归预测到的直线进行作图
import matplotlib.pyplot as plt
plt.scatter(X_train,y_train)
plt1, = plt.plot(xx,yy,label = "Degree = 1") #逗号必须有
plt.axis([0,25,0,25])
'''
xmin, xmax, ymin, ymax = axis([xmin, xmax, ymin, ymax])
'''
plt.xlabel('Diameter of pizza')
plt.ylabel('Price of pizza')
plt.legend(handles = [plt1])
plt.show()

print(regressor.score(X_train,y_train))




from sklearn.preprocessing import PolynomialFeatures
#使用PolynomialFeatures(degree=2)映射出二次多项式特征，存储在变量x_train_poly2中
poly2 = PolynomialFeatures(degree=2)
X_train_poly2 = poly2.fit_transform(X_train)

regressor_poly2 = LinearRegression()
#对二次多项式回归模型进行训练
regressor_poly2.fit(X_train_poly2,y_train)

#从新映射绘图用x轴采样数据
xx_poly2 = poly2.transform(xx)

#使用二次多项式回归模型对应x轴采样数据进行回归预测
yy_poly2 = regressor_poly2.predict(xx_poly2)

#分别对训练数据点、线性回归直线、二次多项式回归曲线进行画图
plt.scatter(X_train,y_train)
plt1, = plt.plot(xx,yy,label = "Degree = 1") #逗号必须有
plt2, = plt.plot(xx,yy_poly2,label = "Degree = 2") #逗号必须有
plt.axis([0,25,0,25])
plt.xlabel('Diameter of pizza')
plt.ylabel('Price of pizza')
plt.legend(handles = [plt1,plt2])
plt.show()

print(regressor_poly2.score(X_train_poly2,y_train))




#使用PolynomialFeatures(degree=4)映射出二次多项式特征，存储在变量x_train_poly2中
poly4 = PolynomialFeatures(degree=4)
X_train_poly4 = poly4.fit_transform(X_train)

regressor_poly4 = LinearRegression()
#对4次多项式回归模型进行训练
regressor_poly4.fit(X_train_poly4,y_train)

#从新映射绘图用x轴采样数据
xx_poly4 = poly4.transform(xx)

#使用4次多项式回归模型对应x轴采样数据进行回归预测
yy_poly4 = regressor_poly4.predict(xx_poly4)

#分别对训练数据点、线性回归直线、二次多项式以及四次多项式回归曲线进行画图
plt.scatter(X_train,y_train)
plt1, = plt.plot(xx,yy,label = "Degree = 1") #逗号必须有
plt2, = plt.plot(xx,yy_poly2,label = "Degree = 2") #逗号必须有
plt4, = plt.plot(xx,yy_poly4,label = "Degree = 4") #逗号必须有
plt.axis([0,25,0,25])
plt.xlabel('Diameter of pizza')
plt.ylabel('Price of pizza')
plt.legend(handles = [plt1,plt2,plt4])
plt.show()

print(regressor_poly4.score(X_train_poly4,y_train))

X_test = [[6],[8],[11],[16]]
y_test = [[8],[12],[15],[18]]

#使用测试集来评估
print(regressor.score(X_test,y_test))

X_test_poly2 = poly2.transform(X_test)
print(regressor_poly2.score(X_test_poly2,y_test))

X_test_poly4 = poly4.transform(X_test)
print(regressor_poly4.score(X_test_poly4,y_test))

#使用L1范数正则化,使用的是Lasso模型
from sklearn.linear_model import Lasso
lasso_poly4 = Lasso()
lasso_poly4.fit(X_train_poly4,y_train)
print(lasso_poly4.score(X_test_poly4,y_test))
#输出Lasso模型的参数类别
print(lasso_poly4.coef_)
#回顾普通四次多项式回归模型过拟合之后的性能
print(regressor_poly4.score(X_test_poly4,y_test))
#回顾普通四次多项式回归模型的参数列表
print(regressor_poly4.coef_)


#使用L2范数正则化,使用的是Ridge模型
#输出普通四次多项式参数的平方和，即参数之间的差异
print(np.sum(regressor_poly4.coef_ ** 2))
from sklearn.linear_model import Ridge
ridge_poly4 = Ridge()
ridge_poly4.fit(X_train_poly4,y_train)
#输出Ridge模型在测试样本上的回归性能
print(ridge_poly4.score(X_test_poly4,y_test))
#输出Ridge模型的参数列表
print(ridge_poly4.coef_)
#输出Ridge模型拟合后参数的平方和
print(np.sum(ridge_poly4.coef_ ** 2))
