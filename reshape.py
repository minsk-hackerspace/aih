import cv2
import numpy as np
from glob import glob


def find_object(obj, image):
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # img_gray = img_rgb

    template = cv2.imread('photos/' + obj + '.jpg',0)
    w, h = template.shape[::-1]

    threshold = 1.0
    flag = True
    loc = ()
    while flag:
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where( res >= threshold)
        print(len(loc[0]))
        if len(loc[0]) < 1:
            threshold -= 0.05
        else:
            break


    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)



    cv2.imshow('Detected',cv2.resize(img_rgb, (480, 270)))
    cv2.waitKey(0)


img_mask = 'photos/pho*.jpg'
images = glob(img_mask)

for image in images:
    find_object('ball', image)
