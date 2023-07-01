import numpy as np
from CI import *
cnt = 0
for _ in range(1000):
    data = np.zeros([3, 1000])
    data[0] = np.random.uniform(low=-1.0, high=1.0, size=1000)
    data[1] = 0.3 * data[0] + np.random.normal(loc=0.0, scale=0.5, size=1000)
    data[2] = 0.5 * data[1] + np.random.uniform(low=-0.3, high=0.3, size=1000)
    for i in range(3):
        data[i] -= np.mean(data[i])
    
    if newCI_test(data, 0, 2, (1,), 0.05)==False:
        cnt += 1
    # if newCI_test(data, 0, 2, (1,), 0.05)==True:
    #     cnt += 1
print(cnt)