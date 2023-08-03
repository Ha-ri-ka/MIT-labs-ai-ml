import cv2 as cv
import numpy as np

img=cv.imread("D:/wallpaper/pics/tile.png")
blank=np.zeros((500,500,3),dtype='uint8')

#we can use a blank image or an actual image to draw on
#uint8-->datatype of an image
#(500,500,3)-->height,width and shape (number of color channels)
# cv.imshow('blank',blank)
#-----------------------------------------------------------
#1. paint the image a certain color
# blank[:]=255,0,0 #set all pixels in blank to red.its (b g r)i think?
# cv.imshow('blue image',blank)
# blank[200:300,300:400]=0,0,255
# cv.imshow('blue with red image',blank)
#-----------------------------------------------------------
#2. draw a rectangle
cv.rectangle(blank,(0,0),(250,500),(0,0,255),2)
# cv.rectangle(blank,(0,0),(250,500),(0,0,255),cv.FILLED) #or-1 in last
# cv.imshow('rectangle',blank)
#-----------------------------------------------------------
cv.circle(blank,(250,250),50,(0,255,255),3)
# cv.imshow('circle',blank)
#-----------------------------------------------------------
cv.line(blank,(0,0),(250,250),(255,255,255),2)
# cv.imshow('line',blank)
#-----------------------------------------------------------
#3. write text on image
cv.putText(blank,'what is done with love is done well',(128,128),cv.FONT_HERSHEY_TRIPLEX,0.5,(255,255,255),1)
cv.imshow('text',blank)
#-----------------------------------------------------------
cv.waitKey(0)