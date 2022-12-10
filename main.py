import numpy as np
import matplotlib.image as mpimg
from skimage.io import imread

from classify import classify
from int_point import int_point
from template_match import template_match


# Helper function to convert to grayscale
def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.144])


search_blank = imread('data/cropped/blank.jpg')
template_blank = imread('data/template_feature/temp_blank.jpg')
x_blank, y_blank = template_match(search_blank, template_blank)
accuracy = classify(x_blank, y_blank)

search_happy = imread('data/cropped/happy.jpg')
template_happy = imread('data/template_feature/temp_happy.jpg')
template_match(search_happy, template_happy)

search_sad = imread('data/cropped/sad.jpg')
template_sad = imread('data/template_feature/temp_sad.jpg')
template_match(search_sad, template_sad)

search_surprise = imread('data/cropped/surprise.jpg')
template_surprise = imread('data/template_feature/temp_surprise.jpg')
template_match(search_surprise, template_surprise)

# Interest Points
img_b = mpimg.imread('data/cropped/blank.jpg')
img_h = mpimg.imread('data/cropped/happy.jpg')
img_s = mpimg.imread('data/cropped/sad.jpg')
img_su = mpimg.imread('data/cropped/surprise.jpg')

blank = rgb2gray(img_b)
int_point(blank)

happy = rgb2gray(img_h)
int_point(happy)

sad = rgb2gray(img_s)
int_point(sad)

surprise = rgb2gray(img_su)
int_point(surprise)
