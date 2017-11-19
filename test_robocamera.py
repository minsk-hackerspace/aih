import robocamera
import cv2

cam = robocamera.RoboCamera('http://100.95.255.181:8090/?action=snapshot','http://100.95.255.181:8091/?action=snapshot')

camL,camR = cam.get_undistorted_images()
if camL is not None:
    cv2.imwrite('/tmp/camL.jpg',camL)
    cv2.imwrite('/tmp/camR.jpg',camR)



