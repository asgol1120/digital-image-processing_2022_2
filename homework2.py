import numpy as np, cv2
import copy
def fun5_colormap_HSV():
    global th, hue, Bgr, Hsv, img_bg
    # 1 load image
    # 2 convert colormap
    img_bg = cv2.imread("weather-map.jpg")
    Bgr = cv2.imread("weatherman-on-green2.jpg", cv2.IMREAD_COLOR)
    Hsv = cv2.cvtColor(Bgr, cv2.COLOR_BGR2HSV) #변환
    hue = np.copy(Hsv[:,:,0])
    cv2.imshow("bgr_input", Bgr) #input image
    cv2.namedWindow("result")
    #3 create trackbars with CB function
    th = [55, 70]
    cv2.createTrackbar("H_thresh1", "result", th[0], 255, onThreshold_H0)
    cv2.createTrackbar("H_thresh2", "result", th[1], 255, onThreshold_H1)
    onThreshold_H0(th[0]) #initial view

def onThreshold_H0(value):
    global res_im
    th[0] = cv2.getTrackbarPos("H_thresh1", "result")
    #thresholding:
    _, res_im = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(res_im, th[0], 255, cv2.THRESH_BINARY, res_im)
    cv2.imshow("result", res_im)
    chromakey()

def onThreshold_H1(value):
    th[1] = cv2.getTrackbarPos("H_thresh2", "result")
    #thresholding:
    _, res_im = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(res_im, th[0], 255, cv2.THRESH_BINARY, res_im)
    cv2.imshow("result", res_im)
    chromakey()

def chromakey():
    global roi

    roi = img_bg[34:442, 170:660]  # 관심 영역(roi) 지정
    mask = cv2.bitwise_not(res_im) #마스크 반전

    image_man = cv2.bitwise_and(Bgr, Bgr, mask=mask)  # 배경 제거한 남자 이미지
    image_bg = cv2.bitwise_and(roi, roi, mask=res_im)  # 마스킹된 배경

    img_bg_copy = copy.deepcopy(img_bg)
    img_bg_copy2 = copy.deepcopy(img_bg)
    img_bg_copy[34:442, 170:660] = image_bg  #마스킹된 배경을 원본에 복사
    cv2.imshow('img_bg', img_bg_copy)

    dst = cv2.add(image_man, image_bg)  # 남자와 배경을 합성
    img_bg_copy2[34:442, 170:660] = dst  # 합성된 영상을 원본(기상지도)에 복사
    cv2.imshow('image-tv', img_bg_copy2)

    cv2.imshow('mask-man', mask)
    cv2.imshow('image-man', image_man)


fun5_colormap_HSV()


cv2.waitKey(0)
cv2.destroyAllWindows()