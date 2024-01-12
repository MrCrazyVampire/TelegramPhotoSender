import cv2
import time 
import requests
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

# _, startFrame = cam.read()
# startFrame = imutils.resize(startFrame, width=500)
# startFrame = cv2.cvtColor(startFrame    , cv2.COLOR_BGR2GRAY)
# startFrame = cv2.GaussianBlur((startFrame),(21,21), 0)

# cv2.imwrite('test.jpg', startFrame)

# while True:
#     _, frame = cam.read()
#     frame = imutils.resize(frame, width=500)
#     frameBW = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     frameBW = cv2.GaussianBlur(frameBW, (5, 5), 0)

#     diffrence = cv2.absdiff(frameBW, startFrame)
#     threshold = cv2.threshold(diffrence, 25, 255, cv2.THRESH_BINARY)[1]
#     startFrame = frameBW
    
#     if threshold.sum() > 300:
#         cv2.imwrite('test.jpg', frameBW)
#     else:
#         cv2.imshow('cam', threshold)
#         cv2.imshow('a',frame) 

#     keypressed = cv2.waitKey(30)
#     if keypressed == ord('q'):
#         break


def sendImage():
    url ="https://api.telegram.org/bot6165779263:AAG5QV0Vj0R9gxqr6lAwrQhIGs_JncPQ8HY/sendPhoto?chat_id=-913458777"
    parameters = {"photo" :""}
    resp = requests.get(url, data=parameters)
    print(resp.status_code)

sendImage()    