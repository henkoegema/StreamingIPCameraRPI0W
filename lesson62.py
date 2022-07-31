#AI ON THE JETSON NANO LESSON 62: CREATE A STREAMING IP CAMERA FROM A RASPBERRY PI ZERO W
#https://www.youtube.com/watch?v=7Bz0QzlK6ps&t=1716s

import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2

#Uncomment These next Two Line for Pi Camera
camSet=' tcpclientsrc host=192.168.2.100 port=8554 ! gdpdepay ! rtph264depay ! h264parse ! nvv4l2decoder  ! nvvidconv flip-method='+str(flip)+' ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+',format=BGR ! appsink  drop=true sync=false '

cam= cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow('nanoCam',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

# The following line activates the Raspberry Pi 0 W camera:
#raspivid -t 0 -w 1296 -h 730 -fps 30 -b 2000000 -awb auto -n  -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=0.0.0.0 port=8554