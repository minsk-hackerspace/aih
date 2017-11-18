print 'GO!'

print("ESC = exit, SPACE = capture...")

import cv2
import numpy as np

cam0 = cv2.VideoCapture(2)
cam1 = cv2.VideoCapture(0)

img_counter = 1

while True:
    ret0, img0 = cam0.read()
    if not ret0:
        break

    ret1, img1 = cam1.read()
    if not ret1:
        break

    s0 = cv2.resize(img0, (480, 270))
    s1 = cv2.resize(img1, (480, 270))
    
    vis = np.concatenate((s0, s1), axis=1)

    cv2.imshow('cams', vis)

    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        #img = np.concatenate((img0, img1), axis=1)
        img_r_name = "cap/img_r{}.png".format(img_counter)
        img_l_name = "cap/img_l{}.png".format(img_counter)
        cv2.imwrite(img_l_name, img0)        
        cv2.imwrite(img_r_name, img1)
        
        print("Capture !")        
        img_counter += 1

cam0.release()
cam1.release()

cv2.destroyAllWindows()