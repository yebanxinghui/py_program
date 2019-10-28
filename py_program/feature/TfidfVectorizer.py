from sklearn.datasets import fetch_20newsgroups
news = fetch_20newsgroups(subset = 'all')

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    news.data, #特征值
    news.target, #标记值
    test_size = 0.25, #因为一般采用25%的数据作为测试集，剩下75%的用于构建训练集合
    random_state = 33
)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vec = TfidfVectorizer()

#使用词频统计的方式将原始训练和测试文本转化为特征向量
X_tfidf_train = tfidf_vec.fit_transform(X_train)
X_tfidf_test = tfidf_vec.transform(X_test)

#使用朴素贝叶斯分类器
from sklearn.naive_bayes import MultinomialNB
mnb_tfidf = MultinomialNB()
#使用朴素贝叶斯分类器对TfidfVectorizer(没有去除停用词)后的训练样本进行参数学习
mnb_tfidf.fit(X_tfidf_train,y_train)
y_predict = mnb_tfidf.predict(X_tfidf_test)

from sklearn.metrics import classification_report
print('The accuracy of classifying 20newsgroups using Naive Bayes(TfidfVectorizer without filtering stopwords):',mnb_tfidf.score(X_tfidf_test,y_test))
print(classification_report(y_test,y_predict,target_names = news.target_names))
