import numpy as np
import matplotlib.pyplot as plt

matrix = np.zeros([100, 300, 3], dtype=np.uint8)
matrix[:,:100] = [255, 0, 0]                # Rojo
matrix[:,100:200] = [255, 255, 255]   # Blanco
matrix[:,200:] = [255, 0, 0]                # Rojo
plt.imshow(matrix)
plt.show()
