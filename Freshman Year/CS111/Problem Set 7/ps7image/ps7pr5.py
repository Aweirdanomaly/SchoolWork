#
# ps7pr5.py  (Problem Set 7, Problem 5)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below
def grayscale(pixels):
    """ takes in a list of [R, G, B] lists 'pixels' and returns it 
    grayscaled"""
    copy = blank_image(len(pixels), len(pixels[0])) 
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            copy[r][c] = pixels[r][c]
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            a = brightness(pixels[r][c])
            copy[r][c][0] = a
            copy[r][c][1] = a
            copy[r][c][2] = a
    return copy

def fold_diag(pixels):
    """ takes in a list of [R, G, B] lists 'pixels' and returns half
    of the image from its diagonal upward"""
    copy = blank_image(len(pixels), len(pixels[0])) 
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            copy[r][c] = pixels[r][c]
    for r in range(len(pixels)):
         for c in range(r):
             copy[r][c] = [255, 255, 255]
    return copy

def mirror_horiz(pixels):
    """ takes in a list of [R, G, B] lists 'pixels' and returns
    it with its right half mirrored"""
    copy = blank_image(len(pixels), len(pixels[0])) 
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            copy[r][c] = pixels[r][c]
    a = len(pixels[0])//2
    for r in range(len(pixels)):
         for c in range(a, len(pixels[0])):
             copy[r][c] = copy[r][-c-1]
    return copy

def extract(pixels, rmin, rmax, cmin, cmax):
    """takes in ints 'rmin', 'rmax', 'cmin', 'cmax' and a list 
    of [R, G, B] lists 'pixels and returns a spliced image within the
    specified dimensions'"""
    copy = blank_image(rmax-rmin, cmax -cmin) 
    for r in range(rmin, rmax):
        for c in range(cmin, cmax):
            copy[r-rmin][c-cmin] = pixels[r][c]
    return copy
    
    
            
            
            