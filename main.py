import cv2 
import mediapipe
import numpy as np
import cv2

def replace_yellow_with_green(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    image[mask > 0] = [0, 255, 0]
    return image
cap = cv2.VideoCapture(0)
while True:
    x, img = cap.read()
    cv2.imshow("video", img)
    cpt=0
    key = cv2.waitKey(1)
    img_out = replace_yellow_with_green(img)
    cv2.imshow("After",img_out)
    if key == ord('q'):
        break
