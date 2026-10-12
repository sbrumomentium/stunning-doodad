import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
image = Image.open("machupicchu.png")
matrix = np.array(image)
plt.imshow(matrix[200:400,:500])
plt.show()

