from imageio import imread
from imageio import imwrite

img = imread("example.jpg")
imwrite("example.png", img, format="png")

