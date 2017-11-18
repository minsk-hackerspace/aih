import robocamera
import cv2

cam = robocamera.RoboCamera('http://192.168.1.14:8090/?action=stream','http://192.168.1.14:8091/?action=stream')

camL,camR = cam.get_undistorted_images()

cv2.imwrite('/tmp/camL.jpg',camL)



