#使用DictVectorizer对字典储存的数据进行特征抽取与向量化
measurements = [{'city':'Dubai','temperature':33.},
                {'city':'London','temperature':12.},
                {'city':'San Fransisco','temperature':18.}]

from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()
#输出转化之后的特征矩阵
print(vec.fit_transform(measurements).toarray())
#输出各个维度的特征含义
print(vec.get_feature_names())
