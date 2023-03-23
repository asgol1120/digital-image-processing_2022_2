import numpy as np, cv2
def fun12_HoughLines():
    #(0) global vars
    global img, gim, wimg, wmap
    #(1) read image
    img = cv2.imread("OntarioHighway.png", cv2.IMREAD_COLOR)
    wimg, wmap = "OntarioHighway", "Edge"
    cv2.namedWindow(wimg, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(wimg, img)
    #(2) convert to grey, and smooth it (for Canny + Hough)
    gim  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gim = cv2.GaussianBlur(gim, (3, 3), 0, 0)
    cv2.imshow(wmap, gim)
    #(3) create 3 track bars
    cv2.createTrackbar("Tbar_1", wmap, thC[0], 255, onThreshold_Canny)
    cv2.createTrackbar("Tbar_2", wmap, thC[1], 255, onThreshold_Canny)
    cv2.createTrackbar("Tbar_3", wmap, thH, 255, onThreshold_Hough)

#2 top level variables
thC = [130, 255] # Canny's thresholds
thH = 130 # Hough's thresdhold

def onThreshold_Canny(value):
    global thC
    thC[0] = cv2.getTrackbarPos("Tbar_1", wmap)
    thC[1] = cv2.getTrackbarPos("Tbar_2", wmap)

    canny = hough_liner() #grim -> canny -< draw lines
    cv2.imshow(wmap, canny)

    res = houghpr_liner()
    cv2.imshow(wimg, res)

def onThreshold_Hough(value):
    global thH
    thH = cv2.getTrackbarPos("Tbar_3", wmap)

    canny = hough_liner()  # grim -> canny -< draw lines
    cv2.imshow(wmap, canny)

    res = houghpr_liner()
    cv2.imshow(wimg, res)

def hough_liner():
    canny = cv2.Canny(gim, thC[0], thC[1])

    lines = cv2.HoughLines(canny, 0.5, np.pi/180, thH)
    white = 255
    for i in range(len(lines)):
        for rho, theta in lines[i]:
            a, b = np.cos(theta), np.sin(theta)
            x0, y0 = a*rho, b*rho
            x1, y1 = int(x0 + 1000*(-b)), int(y0 + 1000*(a))
            x2, y2 = int(x0 - 1000 * (-b)), int(y0 - 1000 * (a))
            cv2.line(canny, (x1, y1), (x2, y2), white, 2)
    return canny

def houghpr_liner():
    canny = cv2.Canny(gim, thC[0], thC[1])
    res = img.copy()

    minLineLength, maxLineGap = 100, 20
    red = (0, 0, 255)

    lines = cv2.HoughLinesP(canny, 0.5, np.pi/180, thH, minLineLength, maxLineGap)
    for i in range(len(lines)):
        for x1, y1, x2, y2 in lines[i]:
            cv2.line(res, (x1, y1), (x2, y2), red, 3)
    return res

fun12_HoughLines()
cv2.waitKey()