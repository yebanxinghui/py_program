#采用朴素贝叶斯方法
from sklearn.datasets import fetch_20newsgroups
#该函数无需预存数据，只需要即时从互联网下载数据
#已经修改该函数，已预存好数据
news = fetch_20newsgroups(subset = 'all')
#查验数据规模和细节
print(len(news.data))
print(news.data[0])


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    news.data, #特征值
    news.target, #标记值
    test_size = 0.25, #因为一般采用25%的数据作为测试集，剩下75%的用于构建训练集合
    random_state = 33
)
'''
X_train ： 训练数据集的特征
X_test ：  测试数据集的特征
y_train ： 训练数据集的标签
y_test ：  测试数据集的标签
'''

#导入用于文本特征向量转化模块
from sklearn.feature_extraction.text import CountVectorizer
vec = CountVectorizer()
X_train = vec.fit_transform(X_train)
X_test = vec.transform(X_test)

#导入朴素贝叶斯模型
from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
mnb.fit(X_train,y_train)
y_predict = mnb.predict(X_test)

from sklearn.metrics import classification_report
print('The accuracy of Naive Bayes Classifier is ',mnb.score(X_test,y_test))
print(classification_report(y_test,y_predict,target_names = news.target_names))

#朴素贝叶斯分类器主要应用于海量互联网文本分类任务
#但是该模型在其他数据特征关联性较强的分类任务上的性能表现不佳
