import cv2 as cv
capture=cv.VideoCapture('C:/Users/OSLAB/Downloads/pinkvenomMV.mp4')
while True:
    _,frame=capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('video',gray)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
# capture.release()
# cv.destroyAllWindows()
