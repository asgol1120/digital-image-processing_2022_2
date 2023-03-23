import numpy as np, cv2

def fun11b_image_viewer():
    #(0)global vars
    global img0, W, H, ws, Hw, ar, wmanhat

    #(1)input
    img0 = cv2.imread("manhattan_big.jpg", cv2.IMREAD_COLOR)

    #(2)get image size, and set viewing paramaters
    H, W = img0.shape[:2]
    ar, ws = H/W, Ww/W
    Hw = int(ar*Ww)
    print('W = {}, H = {}'.format(W, H))

    #(3) window
    wmanhat = "Manhattan"
    cv2.namedWindow(wmanhat, cv2.WINDOW_AUTOSIZE)
    cv2.resizeWindow(wmanhat, Ww, Hw)

    #(4)imshow
    imgw = cv2.resize(img0, (Ww, Hw), cv2.INTER_CUBIC)
    cv2.imshow(wmanhat, imgw)

    # cv2.waitKey(0)

    #(5)set MouseCallback function
    cv2.setMouseCallback(wmanhat, onMouseView)

btn = False
Ww = 600 #viewing window width
vs = 1 #view scale
zs = 4 #zoom scale
h, w = 50*vs, 50*vs

def onMouseView(event, x, y, flag, par):
    global btn
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
        btn = True
    elif event == cv2.EVENT_LBUTTONUP or event == cv2.EVENT_RBUTTONUP:
        btn = False
        imgw = cv2.resize(img0, (Ww, Hw), cv2.INTER_CUBIC)
        cv2.imshow(wmanhat, imgw)
        return
    elif event == cv2.EVENT_MOUSEMOVE:
        if btn == False:
            return

    p = (x, y)
    x0, y0 = int(x/ws), int(y/ws)
    wi, hi = int(w/ws/zs), int(h/ws/zs)
    x1, x2 = x0 - wi, x0 + wi
    y1, y2 = y0 - hi, y0 + hi
    wo, ho = int(w/ws), int(h/ws)
    xz1, xz2 = x0 - wo, x0 + wo
    yz1, yz2 = y0 - ho, y0 + ho

    if x1 < 0:
        dx = -x1
    elif x2 > W:
        dx = W - x2
    else:
        dx = 0

    if y1 < 0:
        dy = -y1
    elif y2 > H:
        dy = H - y2
    else:
        dy = 0

    x1, x2 = x1 + dx, x2 + dx
    y1, y2 = y1 + dy, y2 + dy
    roi = img0[y1:y2, x1:x2]

    if xz1 < 0:
        dx2 = -xz1
    elif xz2 > W:
        dx2 = W - xz2
    else:
        dx2 = 0

    if yz1 < 0:
        dy2 = -yz1
    elif yz2 > H:
        dy2 = H - yz2
    else:
        dy2 = 0

    xz1, xz2 = xz1 + dx2, xz2 + dx2
    yz1, yz2 = yz1 + dy2, yz2 + dy2

    img = np.copy(img0)
    img2x = cv2.resize(roi, (wo * 2, ho * 2), cv2.INTER_LINEAR)
    img[yz1:yz2, xz1:xz2, :] = img2x
    imgw = cv2.resize(img, (Ww, Hw), cv2.INTER_LINEAR)
    cv2.imshow(wmanhat, imgw)

fun11b_image_viewer()
cv2.waitKey(0)