#采用肘部观察法
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

#使用随机均匀分布函数随机出三个簇，每个簇周围有10个数据样本
cluster1 = np.random.uniform(0.5,1.5,(2,10)) #生成2*10的矩阵
cluster2 = np.random.uniform(5.5,6.5,(2,10))
cluster3 = np.random.uniform(3.0,4.0,(2,10))
'''
函数原型：numpy.random.uniform(low,high,size)
功能：从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.
参数介绍: 
    low: 采样下界，float类型，默认值为0；
    high: 采样上界，float类型，默认值为1；
    size: 输出样本数目，为int或元组(tuple)类型，例如，size=(m,n,k), 则输出m*n*k个样本，缺省时输出1个值。

返回值：ndarray类型，其形状和参数size中描述一致。
这里顺便说下ndarray类型，表示一个N维数组对象，其有一个shape（表维度大小）和dtype（说明数组数据类型的对象）
'''

#绘制30个数据样本的分布图像
X = np.hstack((cluster1,cluster2,cluster3)).T #T表述矩阵的转置，现在这里为30*2的矩阵
'''
    两个拼接数组的方法：
    np.vstack():在竖直方向上堆叠
    np.hstack():在水平方向上平铺
'''
plt.scatter(X[:,0],X[:,1])
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()

#测试9种不同聚类中心数量下，每种情况的聚类质量，并作图
K = range(1,10)
meandistortions = []
for k in K:
    kmeans = KMeans(n_clusters = k)
    kmeans.fit(X)
    meandistortions.append(sum(np.min(cdist(X,kmeans.cluster_centers_,'euclidean'),axis = 1))/X.shape[0])
'''
np.min函数参数中的axis缺省则求所有中的最小值,为0则每列的最小值,为1则求每行的最小值
cluster_centers_表示集合中心
cdist(XA, XB, metric='euclidean', p=None, V=None, VI=None, w=None)，该函数用于计算两个输入集合的距离，通过metric参数指定计算距离的不同方式得到不同的距离度量值
'''

plt.plot(K,meandistortions,'bx-')
plt.xlabel('k')
plt.ylabel('Average Dispersion')
plt.title('Selecting k with the Elbow Method')
plt.show()

