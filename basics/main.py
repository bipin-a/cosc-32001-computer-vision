# Method 1: Load an image using OpenCV and display it
import cv2

image_path = 'images/blue.png'
image = cv2.imread(image_path)

cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Method 2: Load an image using Matplotlib and display it
import cv2
from matplotlib import pyplot as plt

img2 = cv2.imread(image_path)
# Convert from BGR to RGB for correct color display
img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
plt.imshow(img2_rgb)
plt.show()

# Method 3: Load an image using skimage and display it
from skimage import io
import matplotlib.pyplot as plt

img = io.imread(image_path)

plt.imshow(img)
plt.axis('off')
plt.show()