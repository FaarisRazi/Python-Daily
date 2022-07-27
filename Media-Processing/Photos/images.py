# Handy image-processing functions to come InshaAllah!
from PIL import Image, ImageOps
import cv2 as cv
import numpy as np

# Invert colors in Image: 
img_invert = lambda x: ImageOps.invert(x.convert('RGB'))

# Resize an Image (automatically with given width)
def img_resize(photo, by_width):
    width, height = photo.size
    wpercent = (by_width/float(width))
    hsize = int((float(height)*float(wpercent)))
    
    photo = photo.resize((by_width, hsize), Image.ANTIALIAS)
    
    return photo
