# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:39:54 2019

@author: System2
"""
"""1)Pillow"""
from PIL import Image
import sys

try:
    tatras = Image.open("tatras.jpg")

except IOError:
    print("Unable to load image")
    sys.exit(1)

tatras.save('tatras.png', 'png')


"""2)Wand"""
from __future__ import print_function
from wand.image import Image
 
with Image(filename='source.pdf') as img:
    print('pages = ', len(img.sequence))
 
    with img.convert('png') as converted:
        converted.save(filename='pyout/page.png')
