#采用k近邻模型
from sklearn.datasets import load_iris
iris = load_iris()
#先查验下数据集的规模
print(iris.data.shape)

#查看数据说明
print(iris.DESCR)
'''
Iris Plants Database
====================

Notes
-----
Data Set Characteristics:
    :Number of Instances: 150 (50 in each of three classes)
    :Number of Attributes: 4 numeric, predictive attributes and the class
    :Attribute Information:
        - sepal(花萼) length in cm
        - sepal width in cm
        - petal(花瓣) length in cm
        - petal width in cm
        - class:
                - Iris-Setosa
                - Iris-Versicolour
                - Iris-Virginica
    :Summary Statistics:

    ============== ==== ==== ======= ===== ====================
                    Min  Max   Mean    SD   Class Correlation
    ============== ==== ==== ======= ===== ====================
    sepal length:   4.3  7.9   5.84   0.83    0.7826
    sepal width:    2.0  4.4   3.05   0.43   -0.4194
    petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)
    petal width:    0.1  2.5   1.20  0.76     0.9565  (high!)
    ============== ==== ==== ======= ===== ====================

    :Missing Attribute Values: None
    :Class Distribution: 33.3% for each of 3 classes.
    :Creator: R.A. Fisher
    :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)
    :Date: July, 1988
    
    一共150多鸢尾花数据样本，平均分布在三个不同的亚种，四种特征，分别是花萼的长度和宽度，花瓣的长度和宽度
'''

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, #特征值
    iris.target, #标记值
    test_size = 0.25, #因为一般采用25%的数据作为测试集，剩下75%的用于构建训练集合
    random_state = 33
)
'''
X_train ： 训练数据集的特征
X_test ：  测试数据集的特征
y_train ： 训练数据集的标签
y_test ：  测试数据集的标签
'''

#应用机器模型前，应该将数据标准化
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

#使用K近邻分类器
from sklearn.neighbors import KNeighborsClassifier
knc = KNeighborsClassifier()
knc.fit(X_train,y_train)
y_predict = knc.predict(X_test)

#查看K近邻的精确性
from sklearn.metrics import classification_report
print('Accuracy of the K-Nearest Neighbor Classifier : ', knc.score(X_test, y_test))
print(classification_report(y_test,y_predict,target_names = iris.target_names))