import numpy as np
import cv2

img = cv2.imread('Lena.png', cv2.IMREAD_GRAYSCALE)

p1 = (-1, -1)   # 2-D point
red, blue = (0, 0, 255), (255, 0, 0)    # 2 colors: bgr
list1 = list()

if img is None:
    print('영상 파일 읽기 오류')
    img = np.random.random((512, 512)) * 255  # 랜덤 영상 만들기
    img = np.uint8(img)


def fun_masking():
    mask = np.zeros(img.shape, np.uint8)  # a mask to be
    pts = np.array(list1, np.int32)  # 클릭한 꼭짓점 배열
    print(pts)
    mask3 = cv2.fillPoly(mask, [pts], (255, 255, 255))  # 마스크

    #cv2.imshow('mask3', mask3)
    cv2.imshow('image-out', cv2.bitwise_and(img, mask3))  # 결과 출력


def onMouse(event, x, y, flags, par):
    global p1, red, blue, c
    if event == cv2.EVENT_LBUTTONDOWN:
        c = red
    elif event == cv2.EVENT_RBUTTONDOWN:
        fun_masking()
    else:
        return
    p = (x, y)
    list1.append(p)
    if p1[0] >= 0:
        cv2.line(img, p1, p, c, 3, cv2.LINE_8)
        cv2.imshow("image-in", img)
    p1 = p

cv2.namedWindow('image-in', cv2.WINDOW_AUTOSIZE)
cv2.imshow("image-in", img)
cv2.setMouseCallback("image-in", onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()


