Line Following Using Image-processing:


import RPi.GPIO as GPIO          
from time import sleep

##################camera
from picamera.array import PiRGBArray
import time
import cv2
import picamera
import numpy as np

#l####################eft motor
in1 = 24
in2 = 23
en = 25
temp1=1
#####################rightmotor
in3 = 17
in4 = 27
enB = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#####################left motor
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
p=GPIO.PWM(en,1000)

#####################rightmotor
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
p2=GPIO.PWM(enB,1000)

####################motor start
p.start(15)
p2.start(15)
print("\n")
print("working properly by camera.....")
print("\n")    


#camera
camera = picamera.PiCamera()
camera.resolution =(192,108)
camera.framerate = 20
rawCapture = PiRGBArray(camera,size=(192,108))
time.sleep(0.1)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Display camera input
    image = frame.array
    cv2.imshow('img',image)

    # Create key to break for loop
    key = cv2.waitKey(1) & 0xFF
    
    # convert to grayscale, gaussian blur, and threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh1 = cv2.threshold(blur,100,255,cv2.THRESH_BINARY_INV)
    
    
    # Erode to eliminate noise, Dilate to restore eroded parts of image
    mask = cv2.erode(thresh1, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    # Find all contours in frame
    something, contours, hierarchy = cv2.findContours(mask.copy(),1,cv2.CHAIN_APPROX_NONE)
        
    
    if len(contours) > 0:
            # Find largest contour area and image moments
        c = max(contours, key = cv2.contourArea)
        M = cv2.moments(c)

        # Find x-axis centroid using image moments
        cx = int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        
        if cx >= 150 and cy>40 and cy<90:
            GPIO.output(in1,10)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,4)
            time.sleep(.05)
            
        if cx < 150 and cx >= 130 and cy>40 and cy<90:
            GPIO.output(in1,10)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            time.sleep(.05)    
            
        if cx < 130 and cx > 70 and cy>40 and cy<90:    
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            time.sleep(.05)
        
        if cx <= 70 and cx > 40 and cy>40 and cy<90:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,10)
            GPIO.output(in4,GPIO.LOW)
            time.sleep(.05)
            
        if cx <= 40 and cy>40 and cy<90:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,4)
            GPIO.output(in3,10)
            GPIO.output(in4,GPIO.LOW)
            time.sleep(.05)
    
    if key == ord("q"):
            break

    rawCapture.truncate(0)
    
    
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)    
    
GPIO.cleanup()
