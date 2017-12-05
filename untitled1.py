#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 14:45:04 2017

@author: Jennifer Jennings

Drawing an image

"""

# Import liberies
import numpy as np
import cv2 

# define size of image

# image of 500 x 500 pix with 3 channels
pic = np.zeros((500,500,3), dtype = 'uint8')

# Draw a rectangle ( image, (x_start,y_start) ,  (x_end,y_end) ,  (col), channels, linetype, shift)
cv2.rectangle( pic, (1,1), (500,120), (255,179,0), 3, lineType = 18, shift = 0 )

# Draw a line
cv2.line(pic, (280,280) , (180,280), (0,0,255),thickness = 4)
cv2.line(pic, (280,280) , (280,180), (0,0,255),thickness = 4)

# Draw a circle
cv2.circle(pic, (280,280), 100, (255,255,255), thickness = 12 )

# Add text 

font = cv2.FONT_HERSHEY_DUPLEX # Get Font
cv2.putText( pic, 'Udemy', (100,100),font, 3, (255,255,255), 4, cv2.LINE_8 )

#cv2.imwrite('paint.png',pic)

# Set up drawing
cv2.imshow('Dark image',pic)
cv2.waitKeyEx()
cv2.destroyWindow()