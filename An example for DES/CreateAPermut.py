#%%
import numpy as np

arr = np.arange(1,65).reshape((7,8))
arr = arr.ravel()
np.random.shuffle(arr)
arr = arr.reshape(7,8)

print(arr)
#%%

import numpy as np

inv_P = np.array([[63,52,56,35,7,45,14,39], 
                [17,64,34,19,51,28,60,12], 
                [37,57,4,27,1,62,48,16],
                [11,59,29,32,21,20,25,49],
                [43,50,5,33,42,10,9,40],
                [55,61,44,23,36,18,58,53],
                [47,15,3,30,46,54,22,2],
                [8,26,13,24,38,6,41,31]])

print(inv_P)




# %%
arr = np.arange(1,8).ravel()
arr2 = np.arange(9,16)
arr3 = np.arange(17,24)
arr4 = np.arange(25,32)
arr5 = np.arange(33, 40)
arr6 = np.arange(41,48)
arr7 = np.arange(49, 56)
arr8 = np.arange(57,64)

