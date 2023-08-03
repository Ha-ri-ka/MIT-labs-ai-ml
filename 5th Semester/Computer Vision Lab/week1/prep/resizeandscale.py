import cv2 as cv

def rescaleFrame(frame,scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

def changeResolution(width,height):
    #works only for live video
    capture.set(3,width)
    capture.set(4,height)
#-----------------------------------------------------------
# img=cv.imread("D:/wallpaper/pics/Wallpaper Sea, 5k, 4k wallpaper, ocean, shore, waves, night, Nature #5737.jfif") 
# cv.imshow('ocean original',img)
# cv.imshow('ocean resized',rescaleFrame(img))   
#-----------------------------------------------------------
capture=cv.VideoCapture(0)
while True:
    isTrue,frame=capture.read()
    cv.imshow('video original',frame)
    cv.imshow('video resized',rescaleFrame(frame))
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
#-----------------------------------------------------------
cv.waitKey(0)