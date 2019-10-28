#使用轮廓系数来进行评价
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

#subplot创建子图，所有的绘画只能在子图上进行，plt表示当前子图，若没有分割则默认创建一个子图
#分割出3*2=6个子图，并在一号子图作图
plt.subplot(3,2,1) #plt.subplot('行','列','编号')

#初始化原始数据点
x1 = np.array([1,2,3,1,5,6,5,5,6,7,8,9,7,9])
x2 = np.array([1,3,2,2,8,6,7,6,7,1,2,1,1,3])
X = np.array(list(zip(x1,x2))).reshape(len(x1),2)
'''
reshape(a,b)表示将数据重新组织成a行b列的矩阵
reshape(a,)第二个参数缺省，则表示重新组织成一维矩阵
reshape(a,b,c,d,...)表示将数据重新组织成a*b*c*d*...维度的矩阵
'''

#在一号子图做出原始数据点阵的分布
plt.xlim([0,10]) #设置横坐标范围为0-10
plt.ylim([0,10]) #设置纵坐标范围为0-10
plt.title('Instances') #设置图像的标题(该图像是用来干什么的)
plt.scatter(x1,x2) #使用散点图

colors = ['b','g','r','c','m','y','k','b']
markers = ['o','s','D','v','^','p','*','+']

clusters = [2,3,4,5,8] #生成的聚类数，即产生的质心数
subplot_counter = 1
sc_scores = []
for t in clusters:
    subplot_counter += 1
    plt.subplot(3,2,subplot_counter) 
    kmeans_model = KMeans(n_clusters = t).fit(X)#n_clusters:整形,缺省值=8,生成的聚类数，即产生的质心数
    
    for i,l in enumerate(kmeans_model.labels_):
        plt.plot(x1[i],x2[i],color = colors[l],marker = markers[l],ls = 'None')
        plt.xlim([0,10])
        plt.ylim([0,10])
    sc_score = silhouette_score(X,kmeans_model.labels_,metric = 'euclidean')
    sc_scores.append(sc_score)
    #绘制轮廓系数与不同类簇数量的直观显示图
    plt.title('K = %s, silhouette coefficient = %0.03f' % (t,sc_score))
'''
silhouette_score计算所有样本的平均轮廓系数。
kmeans_model.labels_ 每个样本的预测标签。即预测的类的标签
metric='euclidean' 用的方法为欧式距离
'''

#绘制轮廓系数与不同类簇数量的关系曲线
plt.figure()  #定义一个图像窗口
plt.plot(clusters,sc_scores,'*-')  #plot函数用来画出曲线，'*-'表示线风格为*-
plt.xlabel('Number of clusters')  #横轴表示属性
plt.ylabel('Silhouette Coefficient Score') #纵轴表示属性
plt.show()  #show函数显示图像

