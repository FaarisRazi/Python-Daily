# Handy image-processing functions to come InshaAllah!
from PIL import Image, ImageOps, ImageChops
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


# Trim Images with empty-spaces (or trim out borders in image)
def img_trim(img):
    bg = Image.new(img.mode, img.size, img.getpixel((0,0)))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        img = img.crop(bbox)
    return img


# Remove White/Black background from Image (to transparent)
def remove_img_background(x, white=True, save=False):
    remove_id = 255 if white else 0
    
    img = x.convert('RGBA')
    img_data = img.getdata()
    
    new_data = []
    for i, item in enumerate(img_data):
        
        if item[0] == remove_id and item[1] == remove_id and item[2] == remove_id:
            new_data.append(tuple([remove_id]*3+[0]))
        else:
            new_data.append(item)
    
    img.putdata(new_data)
#     img = Image.fromarray(np.array(new_data))
    
    if save: 
        img.save('img.png' if isinstance(save, bool) else f'{save}.png')
    
    return img


# Sharpen Image quality 
def img_sharpen(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0, as_img=False):
    """Return a sharpened version of the image, using an unsharp mask."""
    
    if 'PIL.Image.Image' in str(type(image)):
        image = np.array(image)
        
    blurred = cv.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    
    if as_img:
        sharpened = Image.fromarray(sharpened)
    
    return sharpened
