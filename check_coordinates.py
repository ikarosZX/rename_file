"""
Created on Fri Oct 18 21:16:53 2019
@author: ikaros
the form of the content in txt : 118,268,186,267,186,278,118,280,###
"""

import cv2
import numpy as np

imgdir = './img.jpg'
txtdir = './img.txt'

img = cv2.imread(imgdir)
img2 = img.copy()

line1 = []
with open(txtdir,'r') as f:
    txtfile = f.read()
linelist = txtfile.split('\n')
linelist = np.array(linelist)
#print(linelist[31])

for s1 in linelist:
    if s1 != '':
        a = s1.split(',')
        x1 = int(a[0])
        y1 = int(a[1])
        x2 = int(a[2])
        y2 = int(a[3])
        x3 = int(a[4])
        y3 = int(a[5])
        x4 = int(a[6])
        y4 = int(a[7])
        coordinates = np.array([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
        #print('coordinates1:',coordinates.shape)
        coordinates = coordinates.reshape((-1,1,2))
        #print('coordinates2:',coordinates.shape)
        img2 = cv2.polylines(img2,[coordinates],True,(0,255,0),1)

cv2.imshow('img',img2)
cv2.waitKey(0)
