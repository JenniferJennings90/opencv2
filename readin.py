#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:50:02 2017

@author: Jennifer Jennings
"""

import numpy as np
import cv2

# Read in the original Image
img = cv2.imread('flower.jpg') # Read image
  
cv2.imshow('Original', img) # Display Image
cv2.waitKey(0) 
cv2.destroyAllWindows()

# Change the image to grey scale

img = cv2.imread('flower.jpg',0) # Read image
  
cv2.imshow('Original', img) # Display Image
cv2.waitKey(0) 
cv2.destroyAllWindows()


# number > 0: full channels: rgb
img = cv2.imread('flower.jpg',1) # Read image
  
cv2.imshow('Original', img) # Display Image
cv2.waitKey(0) 
cv2.destroyAllWindows()


# number < 0: read as is with alpha channel
img = cv2.imread('flower.jpg',-1) # Read image
  
cv2.imshow('Original', img) # Display Image
cv2.waitKey(0) 
cv2.destroyAllWindows()

