import numpy as np
import cv2

image1 = np.zeros((200, 400), np.uint8)
image1.fill(255)

cv2.imshow('윈도우', image1)
while True:
    key = cv2.waitKey(100)
    if key == 27 :
        break
    elif key == -1:
        continue
    try:
        print('키 값은 ', key)
        # result = switch_case[key]
        # print(result)
    except KeyError:
        result = -1
cv2.destroyAllWindows()