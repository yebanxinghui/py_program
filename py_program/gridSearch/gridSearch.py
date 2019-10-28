#使用单线程对文本分类的朴素贝叶斯模型的超参数组合执行网格搜索
from sklearn.datasets import fetch_20newsgroups
import numpy as np
news = fetch_20newsgroups(subset = 'all')

#对前3000条新闻文本进行数据分割，25%文本用于未来测试
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(news.data[:3000],news.target[:3000],test_size = 0.25,random_state = 33)

#使用支持向量机(分类)模型
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

#使用Pipeline简化系统搭建流程，将文本抽取与分类器模型串联起来
clf = Pipeline([('vect',TfidfVectorizer(stop_words = 'english',analyzer = 'word')),('svc',SVC())])
'''
前一个TfidfVectorizer是一个Transformer
后面的SVC是一个Estimator
pipeline参数一般第一个为特征标准化，最后一个为estimator，并且返回一个estimator对象
'''

#这里需要试验的2个超参数的个数分别是4，3，svc__gamma的参数共有10^-2,10^-1...这样我们一共有12种的超参数组合，12个不同参数下的模型
parameters = {'svc__gamma':np.logspace(-2,1,4),'svc__C':np.logspace(-1,1,3)}
'''
logspace用于创建等比数列的列表
第一个参数是开始点，第二个参数是结束点，第三个参数是元素个数，默认底数base=10
比如np.logspace(0,9,10)表示开始点为10^0,结束点为10^9，元素个数为10
'''

from sklearn.grid_search import GridSearchCV

#将12组参数组合以及初始化的Pipeline包括3折交叉验证的要求全部告知GridSearchCV
#参数refit=True则程序将以交叉验证训练集得到的最佳超参数
gs = GridSearchCV(clf,parameters,verbose = 2,refit = True,cv=3)

#执行单线程网格搜索
#%time _ = gs.fit(X_train,y_train)
'''
ipython是python的一个shell
在命令行打开ipython   
%time是ipython内置的魔法函数，只能在ipython中使用
'''
gs.best_params_,gs.best_score_

#输出最佳模型在测试集上的准确性
print(gs.score(X_test,y_test))

