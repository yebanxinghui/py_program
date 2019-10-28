#使用tensorflow输出一句话
import tensorflow as tf
import numpy as np

#初始化一个TensorFlow的常量：Hello Google Tensorflow!字符串，并命名为greeting作为一个计算模块
greeting = tf.constant('Hello Google Tensorflow! ')

#启动一个会话
sess = tf.Session()
#使用会话执行greeting计算模块
result = sess.run(greeting)
#输出会话执行的结果
print(result)
#关闭会话，这是一种显式关闭会话的方式
sess.close()

