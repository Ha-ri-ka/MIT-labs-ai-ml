import cv2 as cv
import numpy as np
path = "C:/Users/OSLAB/Desktop/images/hog_people/three.jpg"
path="C:/Users/OSLAB/Desktop/images/hog_people/one.jpg"
path="C:/Users/OSLAB/Desktop/images/hog_people/two.webp"

def rescaleFrame(frame, scale=0.5):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    dim = (w, h)
    return cv.resize(frame, dim)

img = cv.imread(path)

hog=cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

if img.shape[1] < 400: 
        (height, width) = img.shape[:2]
        ratio = width / float(width) 
        img = cv.resize(img, (400, width*ratio))

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
rects, weights = hog.detectMultiScale(gray, winStride=(2, 2), padding=(10, 10), scale=1.02)
for i, (x,y,w,h) in enumerate(rects):
    if weights[i]<0.13: continue
    elif weights[i]<0.3 and weights[i] > 0.13:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    elif weights[i] >0.3 and weights[i]<0.7:
        cv.rectangle(img, (x, y), (x+w, y+h), (50, 122, 255), 2)
    if weights[i] < 0.7 and weights[i] > 0.3:
            cv.rectangle(img, (x, y), (x+w, y+h), (50, 122, 255), 2)
    if weights[i] > 0.7:
            cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('Final img', img)
cv.waitKey(0) 
# cv.destroyAllWindows()
