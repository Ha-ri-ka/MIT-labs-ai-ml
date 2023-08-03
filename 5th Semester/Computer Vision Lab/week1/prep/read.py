import cv2 as cv
# img=cv.imread("D:/wallpaper/pics/tile.png")
# cv.imshow('love',img)
#-----------------------------------------------------------
# img=cv.imread("D:/wallpaper/pics/Wallpaper Sea, 5k, 4k wallpaper, ocean, shore, waves, night, Nature #5737.jfif") #too big to display properly, so we could re-size (later)
# cv.imshow('ocean',img)
#-----------------------------------------------------------
capture=cv.VideoCapture(0)
while True:
    isTrue,frame=capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
#-----------------------------------------------------------
cv.waitKey(0)
