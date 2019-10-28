#使用单一决策树，随机森林，梯度上升法决策树三类模型分析泰坦尼克号乘客数据
import pandas as pd
titanic = pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')
#观察前几行数据
titanic.head()
'''
   row.names pclass  survived  \
0          1    1st         1   
1          2    1st         0   
2          3    1st         0   
3          4    1st         0   
4          5    1st         1   

                                              name      age     embarked  \
0                     Allen, Miss Elisabeth Walton  29.0000  Southampton   
1                      Allison, Miss Helen Loraine   2.0000  Southampton   
2              Allison, Mr Hudson Joshua Creighton  30.0000  Southampton   
3  Allison, Mrs Hudson J.C. (Bessie Waldo Daniels)  25.0000  Southampton   
4                    Allison, Master Hudson Trevor   0.9167  Southampton   

                         home.dest room      ticket   boat     sex  
0                     St Louis, MO  B-5  24160 L221      2  female  
1  Montreal, PQ / Chesterville, ON  C26         NaN    NaN  female  
2  Montreal, PQ / Chesterville, ON  C26         NaN  (135)    male  
3  Montreal, PQ / Chesterville, ON  C26         NaN    NaN  female  
4  Montreal, PQ / Chesterville, ON  C22         NaN     11    male  
数据类型各异，数值型，类别型，甚至还有缺失数据NaN
'''

#使用pandas独有的dataframe格式(二维数据表格),使用info查看数据的统计特性
print(titanic.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1313 entries, 0 to 1312
Data columns (total 11 columns):
row.names    1313 non-null int64
pclass       1313 non-null object
survived     1313 non-null int64
name         1313 non-null object
age          633 non-null float64
embarked     821 non-null object
home.dest    754 non-null object
room         77 non-null object
ticket       69 non-null object
boat         347 non-null object
sex          1313 non-null object
dtypes: float64(1), int64(2), object(8)
memory usage: 112.9+ KB
None
'''

#先进行特征的选择
X = titanic[['pclass','age','sex']]
y = titanic['survived']

#对当前选择的特征进行探查
print(X.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1313 entries, 0 to 1312
Data columns (total 3 columns):
pclass    1313 non-null object
age       633 non-null float64
sex       1313 non-null object
dtypes: float64(1), object(2)
memory usage: 30.9+ KB
None
(1)age这个数据列，只有633个，需要补完
(2)sex和pclass这两个数据列的值都是类别型的，需要转化为数值特征，用0/1代替
'''

#先补完age数据列，使用平均数或者中位数都是对模型影响偏离最小的策略
X['age'].fillna(X['age'].mean(),inplace=True) #此处采用平均数填充
print(X.info())

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, #特征值
    y, #标记值
    test_size = 0.25, #因为一般采用25%的数据作为测试集，剩下75%的用于构建训练集合
    random_state = 33
)
'''
X_train ： 训练数据集的特征
X_test ：  测试数据集的特征
y_train ： 训练数据集的标签
y_test ：  测试数据集的标签
'''

#使用特征转换器
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer(sparse = False)

#转换特征后，凡是类别型的特征都单独剥离出来，独成一列特征，数值型的则保持不变
X_train = vec.fit_transform(X_train.to_dict(orient = 'record'))
print(vec.feature_names_)

#同样需要对测试数据的特征进行转换
X_test = vec.transform(X_test.to_dict(orient = 'record'))

#使用单一决策树
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(X_train,y_train)
dtc_y = dtc.predict(X_test)

#使用随机森林分类器,属于集成模型
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)
rfc_y = rfc.predict(X_test)

#使用梯度提升决策树,属于集成模型
from sklearn.ensemble import GradientBoostingClassifier
gbc = GradientBoostingClassifier()
gbc.fit(X_train,y_train)
gbc_y = gbc.predict(X_test)

from sklearn.metrics import classification_report
#单一决策树
print('Accuracy of the dtc: ', dtc.score(X_test, y_test))
print(classification_report(y_test, dtc_y, target_names = ['died','survived']))
#随机森林
print('Accuracy of the rfc: ', rfc.score(X_test, y_test))
print(classification_report(y_test, rfc_y, target_names = ['died','survived']))
#梯度提升决策树
print('Accuracy of the gbc: ', gbc.score(X_test, y_test))
print(classification_report(y_test, gbc_y, target_names = ['died','survived']))
