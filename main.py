import cv2 
import mediapipe
import numpy as np
import cv2
#easy code but it can help us in a lot of things ;)
def replace_yellow_with_green(image):
    #you can change the color
    
    #convert RGB to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #the possible values of yellow
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    #creating a mask
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    #changing the values
    image[mask > 0] = [0, 255, 0]
    
    return image

#webcam
cap = cv2.VideoCapture(0)
while True:
    #reading the cap
    x, img = cap.read()
    
    #you can work with pics using "img = cv2.imread()"
    #showing the video before applying the function
    cv2.imshow("Before", img)
    cpt=0
    key = cv2.waitKey(1)
    img_out = replace_yellow_with_green(img)
    #showing the video after applying the function
    cv2.imshow("After",img_out)
    if key == ord('q'):
        break
