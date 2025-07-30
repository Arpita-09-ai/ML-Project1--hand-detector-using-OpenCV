import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import mediapipe
import serial
import time
c=cv2.VideoCapture(0)
det=HandDetector(staticMode=False,maxHands=2,modelComplexity=1,detectionCon=0.5,minTrackCon=0.5)
try:
    while True:
        bl,img=c.read()
        hands,img=det.findHands(img,draw=True,flipType=True)
        cn=0
        if hands:
            for h in hands:
                fingers=det.fingersUp(h)
                print(fingers)
                cn+=fingers.count(1)
                txt,bx=cvzone.putTextRect(img,"FINGERS:"+str(cn),(100,100),scale=3,thickness=3,colorT=(0,255,0),colorR=(255,0,255),font=cv2.FONT_HERSHEY_COMPLEX,offset=10,border=5)
        cv2.imshow("hand",img)
        if cv2.waitKey(1) & 0xff==ord("q"):
            break
finally:
    c.release()
    cv2.destroyAllWindows()