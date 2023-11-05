import cv2
import numpy as np
import time
import PoseModule as PM

cap = cv2.VideoCapture("AITrainer/barra.mp4")
detector = PM.poseDetector()

while True:
    # success, img= cap.read()
    # img = cv2.resize(img,(1288,728)) #reduce el tamaño de la imagen
    # img = cv2.imread("AITrainer/curls1.jpg")
    img = detector.findPose(img)
    cv2.imshow("Image", img)
    #muestra el video
    cv2.waitKey(1)