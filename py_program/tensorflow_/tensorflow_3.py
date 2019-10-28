#使用tensorflow自定义一个线性费雷器用于对良恶性乳腺癌肿瘤进行预测
import tensorflow as tf
import numpy as np
import pandas as pd

train = pd.read_csv('E:/PythonPackage/csv/breast-cancer-train.csv')#传入训练文件数据存入df_train
test = pd.read_csv('E:/PythonPackage/csv/breast-cancer-test.csv')#传入测试文件数据存入df_test
'''
不要从windows直接复制文件路径,否则字符串前面会自带b'\xe2\x80\xaa'导致文件读入错误
建议手打一遍
'''

#分隔特征与分类目标
X_train = np.float32(train[['Clump Thickness','Cell Size']].T)
y_train = np.float32(train['Type'].T)
X_test = np.float32(test[['Clump Thickness','Cell Size']].T)
y_test = np.float32(test['Type'].T)

#定义一个tensorflow的变量b作为线性模型的截距，同时设置初始值为1.0
b = tf.Variable(tf.zeros([1])) #生成了一个长度为1的全零序列
#定义一个tensorflow的变量w作为线性模型的系数，并设置初始值为-1.0到1.0之间均匀分布的随机数
W = tf.Variable(tf.random_uniform([1,2],-1.0,1.0)) #random_uniform第一个参数是shape大小，这里生成1*2的张量，其元素服从-1.0~1.0的均匀分布

#显示定义这个线性函数
y = tf.matmul(W,X_train) + b

#使用tensorflow中的reduce_mean取得训练集上的均方误差
loss = tf.reduce_mean(tf.square(y-y_train))

#使用梯度下降法估计参数W,b, 并且设置迭代步长为0.01，这个与Scikit-learn中的SGDRegressor类似
optimizer = tf.train.GradientDescentOptimizer(0.01)

#以最小二乘损失为优化目标
train = optimizer.minimize(loss)

#初始化所有变量
init = tf.initialize_all_variables()

#开启tensorflow中的会话
sess = tf.Session()
#执行变量的初始化操作
sess.run(init)

#迭代1000次，训练参数
for step in range(0,1000):
    sess.run(train)
    if step % 200 == 0:
        print(step, sess.run(W), sess.run(b))

#准备测试样本
test_negative = test.loc[test['Type'] == 0][['Clump Thickness','Cell Size']]
test_positive = test.loc[test['Type'] == 1][['Clump Thickness','Cell Size']]

#以最终更新的参数作图
import matplotlib.pyplot as plt
plt.scatter(test_negative['Clump Thickness'],test_negative['Cell Size'],marker='o',s=200,c='red')
plt.scatter(test_positive['Clump Thickness'],test_positive['Cell Size'],marker='x',s=150,c='black')

plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
lx = np.arange(0,12)

#这里我们选择以0.5为分界面
ly = (0.5 - sess.run(b) - lx*sess.run(W)[0][0]) / sess.run(W)[0][1]
plt.plot(lx,ly,color = 'green')
plt.show()