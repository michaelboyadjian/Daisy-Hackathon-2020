from skimage import color
from skimage import io
from PIL import Image  
import PIL  
import numpy as np
import scipy.misc

# dont FUCKING run this
# create all images to grayscale and put them into into a list as numpy arrays
'''
img_ar = []
for i in range(1,53):
    for f in range(1,4):
        img = color.rgb2gray(io.imread('images/week_{}_page_{}.jpg'.format(i,f)))
        img_ar.append(img)
'''
def price_checker(img_gray): 
    # 0.17826431372549018 < red < 0.38051921568627456
    img_gray = color.rgb2gray(io.imread(img_gray))
    print(type(img_gray))
    # dimensions of the numpy array
    x, y = img_gray.shape
    result = img_gray.copy()
    for i in range(0,x):
        for l in range(0, y):
            pixel_color = result[i][l]
            if((pixel_color < 0.17826431372549018) or (pixel_color > 0.38051921568627456)):
                result[i][l] = 1.0
    return result

new = price_checker('flyer_split/week_1_page1_item0.jpeg')

scipy.misc.imsave('outfile.jpg', new)