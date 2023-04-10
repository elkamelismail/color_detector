#Importing libraries
import cv2 
import mediapipe
import numpy as np
import cv2

#Defining func that detect the color and create a mask

def replace_color_with_yellow(image,lower,upper,lower_,upper_):
    #converting the pic form RGB to HSV

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #creating two masks

    mask = cv2.inRange(hsv, lower,upper)
    mask_ = cv2.inRange(hsv,lower_,upper_)
    image[mask > 0] = [0, 255, 255]
    image[mask_ > 0] = [0, 255, 255]

    return image

#webcam

cap = cv2.VideoCapture(0)
flag_ = True

while flag_ == True:
    #Reading and showing the MENU

    menu = cv2.imread("MENU.png")
    cv2.imshow("MENU",menu)

    k = cv2.waitKey(1)

    #red
    if k == ord("r"):
        lower = np.array([0, 70, 50])
        upper = np.array([10, 255, 255])
        lower_ = np.array([170, 70, 50])
        upper_ = np.array([180, 255, 255])
        flag_ = False
        
    #green
    if k == ord("g"):
        lower = np.array([40, 40, 40])
        upper = np.array([70, 255, 255])
        lower_ = np.array([40, 40, 40])
        upper_ = np.array([70, 255, 255])
        flag_ = False

    #blue
    if k == ord("b"):
        lower = np.array([90, 50, 50])
        upper = np.array([130, 255, 255])
        lower_ = np.array([90, 50, 50])
        upper_ = np.array([130, 255, 255])
        flag_ = False


while True:
    #reading the cap
    x, img = cap.read()

    #you can work with pics using "img = cv2.imread()"
    #showing the video before applying the function
    cv2.imshow("video", img)
    key = cv2.waitKey(1)
    img_out = replace_color_with_yellow(img,lower,upper,lower_,upper_)
    #showing the video after applying the function
    cv2.imshow("After",img_out)
    if key == ord('q'):
        break
