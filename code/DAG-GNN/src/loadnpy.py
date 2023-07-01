import numpy as np

# 注意编码方式
pre_train = np.load("data1.npy", allow_pickle=True, encoding="latin1")

print("------type-------")
print(type(pre_train))
print("------shape-------")
print(pre_train.shape)
print("------data-------")
print(pre_train)
