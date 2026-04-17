import cv2
import numpy as np
import time
import math

path="cars moving.mp4"
cap=cv2.VideoCapture(path)

backgroundobject=cv2.createBackgroundSubtractorMOG2(detectShadows=False)
kernel=None
##############
###########
while(1):
    ret,frame=cap.read()
    if not ret:
        break
    fmask=backgroundobject.apply(frame)
    _,fmask=cv2.threshold(fmask,250,255,cv2.THRESH_BINARY)
    fmask1=cv2.erode(fmask,kernel,iterations=6)
    fmask2 = cv2.dilate(fmask1, kernel, iterations=4)
    countours,_=cv2.findContours(fmask2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in countours:
        if cv2.contourArea(cnt) >1200:
            x,y,w,h=cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.putText(frame, "Car Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 1, cv2.LINE_AA)
    real_part=cv2.bitwise_and(frame,frame,mask=fmask)
    fmask_f=cv2.cvtColor(fmask,cv2.COLOR_GRAY2BGR)
    stacked=np.hstack((fmask_f,frame,real_part))
    #cv2.imshow("All windows",cv2.resize(stacked,None,fx=0.65,fy=0.65))
    cv2.imshow("two", cv2.resize(fmask_f,(400,400)))
    cv2.imshow("one", cv2.resize(real_part,(400,400)))
    cv2.imshow("three", cv2.resize(frame, (400, 400)))
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



