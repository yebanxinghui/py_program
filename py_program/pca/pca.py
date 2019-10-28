#用PCA即主成分分析将64维度的手写体数字图像信息压缩在二维空间内

import numpy as np
#初始化一个2x2的线性相关矩阵
M = np.array([[1,2],[2,4]])
#计算该矩阵的秩
print(np.linalg.matrix_rank(M,tol = None))

import pandas as pd
#从互联网直接读入手写体图片识别任务的数据
digits_train = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra',header = None)
digits_test = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tes',header = None)

#分割训练数据的特征向量和标记
X_digits = digits_train[np.arange(64)]
y_digits = digits_train[64]

from sklearn.decomposition import PCA
estimator = PCA(n_components = 2)
X_pca = estimator.fit_transform(X_digits)

#显示10累手写体数字图片经过PCA压缩后的二维空间分布
from matplotlib import pyplot as plt

def plot_pca_scatter():
    colors = ['black','blue','purple','yellow','white','red','lime','cyan','orange','gray']
    
    for i in range(len(colors)):
        px = X_pca[:,0][y_digits.as_matrix() == i]
        py = X_pca[:,1][y_digits.as_matrix() == i]
        plt.scatter(px,py,c = colors[i])
        
    plt.legend(np.arange(0,10).astype(str))
    plt.xlabel('First Principal Component')
    plt.ylabel('Second Principal Component')
    plt.show()
plot_pca_scatter()

#对训练数据和测试数据进行特征向量的与分类目标的分割
X_train = digits_train[np.arange(64)]
y_train = digits_train[64]
X_test = digits_test[np.arange(64)]
y_test = digits_test[64]

#使用线性分类器
from sklearn.svm import LinearSVC
svc = LinearSVC()
svc.fit(X_train,y_train)
y_predict = svc.predict(X_test)

#使用PCA将原来的64维图像数据压缩到20个维度
estimator = PCA(n_components = 20)

#利用训练特征决定20个正交维度的方向，并转化原来的训练特征
pca_X_train = estimator.fit_transform(X_train)
#测试特征也按照上述的20个正交维度方向进行转化
pca_X_test = estimator.transform(X_test)

pca_svc = LinearSVC()
pca_svc.fit(pca_X_train,y_train)
pca_y_predict = pca_svc.predict(pca_X_test)

#对使用原始图像高像素特征的支持向量机分类器的性能做出评价
from sklearn.metrics import classification_report
print(svc.score(X_test,y_test))
print(classification_report(y_test,y_predict,target_names = np.arange(10).astype(str)))

#对使用PCA压缩重建的低维图像特征训练的支持向量机分类器的性能做出评估
print(pca_svc.score(pca_X_test,y_test))
print(classification_report(y_test,pca_y_predict,target_names = np.arange(10).astype(str)))

