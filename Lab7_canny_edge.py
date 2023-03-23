import numpy as np, cv2
th = [100, 150]
def fun7_Canny():
    #(1) input
    global img
    img = imread_Lena_gray()
    cv2.imshow("Image_input", img)
    cv2.waitKey(0)

    #(2) window & trackbars - Canny's output
    cv2.namedWindow("WinCanny", cv2.WINDOW_AUTOSIZE)
    cv2.createTrackbar("Tbar_1", "WinCanny", th[0], 255, onThreshold_Canny0)
    cv2.createTrackbar("Tbar_2", "WinCanny", th[1], 255, onThreshold_Canny1)
    cv2.waitKey(0)
    #initial Canny


def imread_Lena_gray():
    img = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("영상 파일 읽기 오류")
        img = np.random.random(512, 512) * 205
        img = np.uint8(img)
    return img


def onThreshold_Canny0(value):
    #read trackbar position
    th[0] = cv2.getTrackbarPos("Tbar_1", "WinCanny")

    #compute the Canny edge
    canny = cv2.Canny(img, th[0], th[1])
    cv2.imshow("WinCanny", canny)


def onThreshold_Canny1(value):
    #read trackbar position
    th[1] = cv2.getTrackbarPos("Tbar_2", "WinCanny")

    #compute the Canny edge
    canny = cv2.Canny(img, th[0], th[1])
    cv2.imshow("WinCanny", canny)


fun7_Canny()