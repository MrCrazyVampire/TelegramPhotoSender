import cv2, time
from datetime import datetime
import os
import requests

now = datetime.now()
current_time = now.strftime("%H:%M")


cam = cv2.VideoCapture(0)

ext = "jpg"
base_path = r"C:/Users/igaur/OneDrive/Documents/code/pictures"
firstFrame = None
os.makedirs(base_path, exist_ok=True)
base_path = os.path.join(base_path, "capture")

def sendImage():
    url ="https://api.telegram.org/bot6165779263:AAG5QV0Vj0R9gxqr6lAwrQhIGs_JncPQ8HY/sendPhoto?chat_id=-913458777"
    # resp = requests.get(url, data=parameters)
    resp = requests.post(url,files={'photo': open('{}_{}.{}'.format(base_path, current_time, ext), 'rb')})
    print(resp.status_code)    


time.sleep(3)
while True:
    check,frame = cam.read(0)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey,(21,21), 0)
    if firstFrame is None:
        firstFrame = grey
        continue
    deltaFrame=cv2.absdiff(firstFrame,grey)
    thresholdFrame=cv2.threshold(deltaFrame,50,255,cv2.THRESH_BINARY)[1]
    thresholdFrame=cv2.dilate(thresholdFrame,None ,iterations=20)   

    contour = cv2.findContours(thresholdFrame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    
    for acontour in contour:
        if cv2.contourArea(acontour)<1500:
            continue 
        (x,y,w,h)=cv2.boundingRect(acontour)
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,255,0), 3)


    if thresholdFrame.sum() > 8000000:
        print('okay')
        cv2.imwrite('{}_{}.{}'.format(base_path, current_time, ext), frame)
        img =   cv2.imread('{}_{}.{}'.format(base_path, current_time, ext))
        sendImage()
        time.sleep(1)
        check,frame = cam.read(0)

        #cv2.imshow('img', img)

        

    cv2.imshow('abcd', frame)   
    key= cv2.waitKey(1)
    if key==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

def sendPictureToAlexa():
    ()

