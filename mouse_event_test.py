import numpy as np
import cv2

img = np.full((300, 500, 3), (255, 255, 255), np.uint8)
p1 = (-1, -1)   # 2-D point
red, blue = (0, 0, 255), (255, 0, 0)    # 2 colors: bgr




def onMouse(event, x, y, flags, par):
    global p1, red, blue
    if event == cv2.EVENT_LBUTTONDOWN:
        c = red
    elif event == cv2.EVENT_RBUTTONDOWN:
        c = blue
    else:
        return
    p = (x, y)
    if p1[0] >= 0:
        cv2.line(img, p1, p, c, 3, cv2.LINE_8)
        cv2.imshow("Canvas", img)
    p1 = p


cv2.imshow("Canvas", img)
cv2.setMouseCallback("Canvas", onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()