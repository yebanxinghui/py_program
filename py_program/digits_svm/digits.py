#从sklearn.datasets里导入手写体数字加载器
from sklearn.datasets import load_digits
digits = load_digits()
#检视数据规模和特征维度
print(digits.data.shape)
'''
(1797, 64)
说明该手写体数字的数码图像数据一共有1797条，并且每幅图是由8x8=64像素矩阵表示的
'''

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, #特征值
    digits.target, #标记值
    test_size = 0.25, #因为一般采用25%的数据作为测试集，剩下75%的用于构建训练集合
    random_state = 33
)
'''
X_train ： 训练数据集的特征
X_test ：  测试数据集的特征
y_train ： 训练数据集的标签
y_test ：  测试数据集的标签
'''

#查验训练样本和测试样本的数量和类别分布
'''
y_train.shape
(1347,)
y_test.shape
(450,)
'''

#应用机器模型前，应该将数据标准化
#即保证每个特征的数值转化为均值为0，方差为1的数据(其实就是归一化，使数据位于-1~1之间)，使训练出的模型不会被某些维度过大的值主导。
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train = ss.fit_transform(X_train) # fit_transform for train data
X_test = ss.transform(X_test)

#这里我们选择支持向量机回归svm模型
from sklearn.svm import LinearSVC
lsvc = LinearSVC()
lsvc.fit(X_train, y_train)
svm_y = lsvc.predict(X_test)

#查看svm的精确性
from sklearn.metrics import classification_report
print('Accuracy of the svm: ', lsvc.score(X_test, y_test))
print(classification_report(y_test, svm_y, target_names = digits.target_names.astype(str)))