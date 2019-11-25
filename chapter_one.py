# import numpy as np
# a = np.array([0, 1, 2, 3, 4, 5])
# print(a)
# b = a.ndim
# print(b)
# c = a.shape
# print(c)
#
# d = a.reshape((3, 2))
# print(d)
# print(d.ndim)
# print(d.shape)

# 两种复制情况，第一种会改变数组a的值，
# 第二种不会改变数组a的值
# 第一种
# a = np.array([0, 1, 2, 3, 4, 5])
# b = a.reshape((3, 2))
# print(b)
# b[1][0] = 77
# print(a)
# print(b)

# 第二种 c和a是完全独立的副本
# a = np.array([0, 1, 2, 3, 4, 5])
# c = a.reshape((3, 2)).copy()
# print(c)
# c[0][0] = 10
# print(a)
# print(c)


# NumPy数组还有一大优势，即对数组的操作可以传递到每一个元素上
# a = np.array([

import scipy as sp
data = sp.genfromtxt("data_one\web_traffic.tsv", delimiter="\t")
# print(data[:30])
# print(data.shape)
# 将各维度分成两个向量
# x包含小时信息
x = data[:, 0]

# y包含某个小时内的web访问数
y = data[:, 1]
print(x)
print(y)

# 有多少小时的数据包含了无效值
num = sp.sum(sp.isnan(y))
print(num)
