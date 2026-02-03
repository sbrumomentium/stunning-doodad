
import numpy as np
import matplotlib.pyplot as plt

fls= 255
cols=255
matrix =np.zeros((fls,cols,3),dtype=np.uint8)
for i in range(fls):
    for j in range(cols):
        matrix[i][j]=[0,0,255]
plt.imshow(matrix)
plt.show()