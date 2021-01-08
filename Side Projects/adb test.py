# -*- coding: utf-8 -*-
"""
Created on Sat May 23 07:21:40 2020

@author: Carlos
"""

from ppadb.client import Client
from PIL import Image
import numpy as np

golden_pixel = 0, 0, 0 ,0 

def main(OGP, adb, device):


    length, height = Screen_Resolution(device)
        
    
    image = device.screencap()
    
    
    
    with open('screen.png', 'wb') as x:
        x.write(image)
    
    image = Image.open('screen.png')
    image = np.array(image, dtype=np.uint8)
    
    
    
    #GOLDEN PIXEL 360, 985
    golden_pixel = image[985, 360] 
    print("previous" , OGP)
    print(golden_pixel)
    
    if np.array_equal(OGP , golden_pixel):
        device.shell('input touchscreen swipe 340 500 340 500 1000')
    
    return golden_pixel


def main_backup(device):
    while True:
        device.shell('input touchscreen swipe 340 500 340 500 100')
        device.shell('sleep .805')
    

def Check_device():
    adb = Client(host='127.0.0.1', port=5037)
    devices = adb.devices()
    
    if len(devices) == 0:
        print("Can't see a phone")
        quit()
        
    device = devices[0]
    return adb, device
    
def Screen_Resolution(device):
    resolution = device.shell('wm size')
    #Omit Physical size:
    resolution = resolution[15:]

    for x in range(0,len(resolution)):
        if resolution[x] == 'x':
            divide = x
        
    length = int(resolution[0:divide])
    height = int(resolution[divide+1:])
    
    return length, height


running = True
adb, device = Check_device()
main_backup(device)
# while (running):
    # if ():
    #     running = False
    #golden_pixel = main(golden_pixel, adb, device)
    

