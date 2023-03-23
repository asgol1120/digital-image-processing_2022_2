import numpy as np, cv2
def fun11_image_viewer():
    #(0)global vars
    global img0, W, H, wmanhat

    #(1)input
    img0 = cv2.imread("manhattan_2towers.jpg", cv2.IMREAD_COLOR)
    wmanhat = "Manhattan"
    cv2.namedWindow(wmanhat, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(wmanhat, img0)
    #cv2.waitKey(0)

    #(2)get image size, and set viewing paramaters
    H, W = img0.shape[:2]
    print('W = {}, H = {}'.format(W, H))

    #(3)set MouseCallback function
    cv2.setMouseCallback(wmanhat, onMouseView)

btn = False
vs = 1 #view scale
zs = 2 #zoom scale
h, w = 25*vs, 25*vs

def onMouseView(event, x, y, flag, par):
    global btn
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
        btn = True
    elif event == cv2.EVENT_LBUTTONUP or event == cv2.EVENT_RBUTTONUP:
        btn = False
        cv2.imshow(wmanhat, img0)
        return
    elif event == cv2.EVENT_MOUSEMOVE:
        if btn == False:
            return

    p = (x, y)
    x1, x2 = x - w, x + w
    y1, y2 = y - h, y + h
    xz1, xz2 = x - w*zs, x + w*zs
    yz1, yz2 = y - h*zs, y + h*zs

    if x1 < 0:
        dx = -x1
    elif x2 > W:
        dx = W - x2
    else:
        dx = 0

    if y1 < 0:
        dy = -y1
    elif y2 > H:
        H - y2
    else:
        dy = 0

    x1, x2 = x1 + dx, x2 + dx
    y1, y2 = y1 + dy, y2 + dy

    if xz1 < 0:
        dx2 = -xz1
    elif xz2 > W:
        dx2 = W - xz2
    else:
        dx2 = 0

    if yz1 < 0:
        dy2 = -yz1
    elif yz2 > H:
        H - yz2
    else:
        dy2 = 0

    xz1, xz2 = xz1 + dx2, xz2 + dx2
    yz1, yz2 = yz1 + dy2, yz2 + dy2

    roi = img0[y1:y2, x1:x2]
    img = np.copy(img0)
    img2x = cv2.resize(roi, (w*zs*2, h*zs*2), cv2.INTER_LINEAR)
    img[yz1:yz2, xz1:xz2, :] = img2x
    cv2.imshow(wmanhat, img)


fun11_image_viewer()
cv2.waitKey(0)