import cv2
import time
import numpy as np

mirror = False
cam_l = cv2.VideoCapture(2)
cam_r = cv2.VideoCapture(0)

i = 0

while True:
    ret_val_a, img_l = cam_l.read()
    ret_val_b, img_r = cam_r.read()
    if mirror:
        img_l = cv2.flip(img_l, 1)
        img_r = cv2.flip(img_r, 1)

    h, w = img_l.shape[:2]
    # print(h, w)

    cv2.line(img_l, (w/2, h/2-h/10), (w/2, h/2+h/10), (0, 255, 0), 2)
    cv2.line(img_r, (w/2, h/2-h/10), (w/2, h/2+h/10), (0, 255, 0), 2)

    cv2.line(img_l, (w/2-w/10, h/2), (w/2+w/10, h/2), (0, 255, 0), 2)
    cv2.line(img_r, (w/2-w/10, h/2), (w/2+w/10, h/2), (0, 255, 0), 2)

    s0 = cv2.resize(img_l, (960, 540))
    s1 = cv2.resize(img_r, (960, 540))

    vis = np.concatenate((s0, s1), axis=1)

    cv2.imshow('cams', vis)
    i += 1
    # print i
    # time.sleep(3)
    if cv2.waitKey(1) == 27:
        break  # esc to quit
    else:
        if mirror:
            img_l = cv2.flip(img_l, 1)
            img_r = cv2.flip(img_r, 1)
        # cv2.imwrite('png_dual/' + str(i) + '_200_l.png', img_l)
        # cv2.imwrite('png_dual/' + str(i) + '_200_r.png', img_r)

cv2.destroyAllWindows()
