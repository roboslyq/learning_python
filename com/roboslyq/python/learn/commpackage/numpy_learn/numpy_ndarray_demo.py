import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([[1, 2, 3], [1, 2, 3]])
print(b)

# 最小维度
a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)

# dtype 参数
a = np.array([1, 2, 3], dtype=complex)
print(a)
