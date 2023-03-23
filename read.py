import numpy as np
import cv2
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    raise Exception("카메라 안됨")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0) # 자동 초점 중지
cap.set(cv2.CAP_PROP_BRIGHTNESS, 100) # 밝기 초기화
cap.set(cv2.CAP_PROP_ZOOM, 1) # digital zoom
frame_rate = cap.get(cv2.CAP_PROP_FPS)