import numpy as np
a = np.empty(9, dtype=np.int64)
a.sort()
b = a.reshape(3, 3)
int_sum = sum(b)
print(int_sum)
c = np.array([128, 300, 56])
result = int_sum / c
print(result)
result = np.int64(result)
print(result)
