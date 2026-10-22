from encodings import iso2022_jp

import numpy as np
import matplotlib.pyplot as plt
fils = 255
cols = 255
matrix = np.zeros([fils, cols,3],dtype=np.uint8)
for i in range(fils):
    for j in range(cols):
        # matrix[i][j] = [0, 0, 255]
        # matrix[i][j] = [0, 0, i]
        # matrix[i][j] = [i,0,j]
        # matrix[i][j] = [i, j, 0]
        # if i % 5 == 0 or j % 5 == 0:
        #     matrix[i][j] = [255, 255, 255]
        # else:
        #     matrix[i][j] = [0, 0, 0]

plt.imshow(matrix)
plt.show()
