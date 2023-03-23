import numpy as np, cv2
def fun5_colormap_HSV():
    global th, hue, Bgr, Hsv, img_bgr, roi
    # 1 load image
    # 2 convert colormap
    img_bgr = cv2.imread("weather-map.jpg")
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

    h, w = Bgr.shape[:2]
    roi = img_bgr[0:h, 0:w]


def onThreshold_H0(value):
    global res_im
    th[0] = cv2.getTrackbarPos("H_thresh1", "result")
    #thresholding:
    _, res_im = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(res_im, th[0], 255, cv2.THRESH_BINARY, res_im)
    cv2.imshow("result", res_im)
    #chroma_key

def onThreshold_H1(value):
    th[1] = cv2.getTrackbarPos("H_thresh2", "result")
    #thresholding:
    _, res_im = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(res_im, th[0], 255, cv2.THRESH_BINARY, res_im)
    cv2.imshow("result", res_im)
    #chroma_key

def chromakey():
    mask = cv2.bitwise_not(res_im) #마스크 반전
    cv2.imshow('mask-man', mask)
    cv2.imshow('image-man', cv2.bitwise_and(Bgr, Bgr, mask=mask))
    cv2.imshow('image-bg', cv2.bitwise_and(roi, roi, mask=res_im))
    cv2.imshow('image-tv', cv2.bitwise_and(Bgr, Bgr, mask=mask) + cv2.bitwise_and(roi, roi, mask=res_im))

fun5_colormap_HSV()
chromakey()

cv2.waitKey(0)
cv2.destroyAllWindows()