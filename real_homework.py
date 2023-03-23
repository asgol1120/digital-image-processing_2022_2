import numpy as np
import cv2
p1 = (-1, -1)
red, blue = (0, 0, 255), (255, 0, 0)
c = red
p0 = p1
ptv = np.array([[0, 0]])
n = 0 # the number of points

def onMouse(event, x, y, flag, par):
    global p1, red, blue, c, p0, ptv, n
    if event == cv2.EVENT_LBUTTONDOWN:
        c = red
    elif event == cv2.EVENT_RBUTTONDOWN:
        #c = blue
        if n > 0:
            p = (x, y)
            cv2.line(img0, p1, p, c, 3, cv2.LINE_8)
            cv2.line(img0, p0, p, c, 3, cv2.LINE_8)
            cv2.imshow("image-in", img0)
            ptv = np.append(ptv, [[x,y]], axis=0)
            n = n + 1
            print('ptv = ', ptv)
            p1 = (-1, -1)
            n = 0
            mask = np.zeros(img0.shape, np.uint8)
            mask = cv2.fillPoly(mask, [ptv], 255)

            # 여기서 부터 빈칸
            img_r = np.random.random((512, 512)) * 255  # 배경으로 사용할 랜덤생성 이미지
            img_r = np.uint8(img_r)
            mask2 = cv2.fillPoly(img_r, [ptv], 0) #배경이미지 자르기

            cv2.namedWindow('image-in', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('image-in', img0)  # 입력 이미지
            cv2.imshow('image-out1', cv2.bitwise_and(img_copy, mask))  # 자른 이미지
            cv2.imshow('image-out2', mask2)  # 자른 배경 이미지
            cv2.imshow('image-out3', cv2.bitwise_or(mask2, cv2.bitwise_and(img_copy, mask)))  # 자른 이미지와 배경이미지 합침
            # 빈칸 끝

        else:
            print('$ Points too few!')
        return
    else:
        return
    p = (x, y)
    if p1[0] >= 0:
        cv2.line(img0, p1, p, c, 3, cv2.LINE_8)
        cv2.imshow("image-in", img0)
        ptv = np.append(ptv, [[x,y]], axis=0)
        n = n + 1
    else:
        ptv = np.array([[x,y]])
        n = 1
        p0 = p
    p1 = p


#  top level code
img0 = cv2.imread('Lena.png', cv2.IMREAD_GRAYSCALE)
img_copy = cv2.imread('Lena.png', cv2.IMREAD_GRAYSCALE)  # img보존

if img0 is None:
    print('영상 파일 읽기 오류')
    img0 = np.random.random((512, 512)) * 255
    img0 = np.uint8(img0)

print('img0: ', img0.shape)
cv2.namedWindow('image-in', cv2.WINDOW_AUTOSIZE)
cv2.imshow("image-in", img0)

fun = 2
if fun == 1:
    fun_masking()
elif fun == 2:
    cv2.setMouseCallback("image-in", onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()