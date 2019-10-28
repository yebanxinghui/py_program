import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

digits_train = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra',header = None)
digits_test = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tes',header = None)

#从训练集合测试集上都分离出64维度的像素特征与1维度的数字目标
X_train = digits_train[np.arange(64)]
y_train = digits_train[64]
X_test = digits_test[np.arange(64)]
y_test = digits_test[64]

from sklearn.cluster import KMeans

#设置聚类中心数量为10
kmeans = KMeans(n_clusters = 10)
kmeans.fit(X_train,y_train)
#此处为逐条判断每个测试图像所属的聚类中心
y_pred = kmeans.predict(X_test)

#使用ARI进行估计
from sklearn import metrics
print(metrics.adjusted_rand_score(y_test,y_pred))
