# coding = utf-8
from __future__ import print_function, unicode_literals
from PIL import Image

img1 = Image.open('2bs.png')
im1 = img1.load()
img2 = Image.open('b2.png')
im2 = img2.load()

w,h = img1.size

count = 0
for x in range(w):
    for y in range(h):
        if(im1[x,y] != im2[x,y]):
            print(im1[x,y],im2[x,y],im1[x,y][2]-im2[x,y][2])
            count += 1
print(count)            

