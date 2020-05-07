from PIL import Image
from os import listdir, makedirs
from os.path import isfile, join
import numpy as np
import cv2

path = 'data/JPEGImages/'
makedirs('data/JPEGImages_Grayscale', exist_ok=True)
files = [f for f in listdir(path) if isfile(join(path, f))]
for file_name in files:
    image = Image.open(join(path, file_name)).convert('L')
    img = np.array(image, 'uint8')
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    cv2.imwrite(join('data/JPEGImages_Grayscale', file_name), img)
