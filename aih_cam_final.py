import cv2
import sys
import numpy as np

#####################################################################

keep_processing = True;
camera_to_use = 0; # 0 if you have no built in webcam, 1 otherwise
# camera_to_use = cv2.CAP_XIAPI; # for the Xiema cameras (opencv built with driver)

#####################################################################

def show_images(frameL,frameR):
    

    h, w = frameL.shape[:2]
    # print(h, w)

    cv2.line(frameL, (w/2, h/2-h/10), (w/2, h/2+h/10), (0, 255, 0), 2)
    cv2.line(frameR, (w/2, h/2-h/10), (w/2, h/2+h/10), (0, 255, 0), 2)

    cv2.line(frameL, (w/2-w/10, h/2), (w/2+w/10, h/2), (0, 255, 0), 2)
    cv2.line(frameR, (w/2-w/10, h/2), (w/2+w/10, h/2), (0, 255, 0), 2)

    #s0 = cv2.resize(frameL, (960, 540))
    #s1 = cv2.resize(frameR, (960, 540))

    #vis = np.concatenate((s0, s1), axis=1)

    #cv2.imshow('cams', vis)
    
    
    s0 = cv2.resize(frameL, (720, 405))
    s1 = cv2.resize(frameR, (720, 405))

    vis = np.concatenate((s0, s1), axis=1)

    cv2.imshow("imgs",vis);
    

# STAGE 1 - open 2 connected cameras

# define video capture object
# cv2.destroyAllWindows()
camL = cv2.VideoCapture();
camR = cv2.VideoCapture();
# cv2.destroyAllWindows()
# exit(0)
# camR = camL
# define display window names

windowNameL = "LEFT Camera Input"; # window name
windowNameR = "RIGHT Camera Input"; # window name

print("s : swap cameras left and right")
print("c : continue to next stage")

if ((camL.open(camera_to_use)) and (camR.open(camera_to_use + 2))):

    while (keep_processing):

        # grab frames from camera (to ensure best time sync.)

        camL.grab();
        camR.grab();

        # then retrieve the images in slow(er) time
        # (do not be tempted to use read() !)

        ret, frameL = camL.retrieve();
        ret, frameR = camR.retrieve();

        # display image

        #cv2.imshow(windowNameL,frameL);
        #cv2.imshow(windowNameR,frameR);
        show_images(frameL,frameR)
        # start the event loop - essential

        # cv2.waitKey() is a keyboard binding function (argument is the time in milliseconds).
        # It waits for specified milliseconds for any keyboard event.
        # If you press any key in that time, the program continues.
        # If 0 is passed, it waits indefinitely for a key stroke.
        # (bitwise and with 0xFF to extract least significant byte of multi-byte response)

        key = cv2.waitKey(40) & 0xFF; # wait 40ms (i.e. 1000ms / 25 fps = 40 ms)

        # It can also be set to detect specific key strokes by recording which key is pressed

        # e.g. if user presses "x" then exit

        if (key == ord('c')):
            keep_processing = False;
        elif (key == ord('s')):
            # swap the cameras if specified
            tmp = camL;
            camL = camR;
            camR = tmp;

else:
    print("Cannot open pair of cameras connected.")

#####################################################################

# STAGE 2: perform intrinsic calibration (removal of image distortion in each image)


print()
print("--> Setup Done")

camera_matrix_l = np.loadtxt("CameraCalibrated/_camera_matrix_l.txt",np.float32)
print(camera_matrix_l)
camera_matrix_r = np.loadtxt("CameraCalibrated/_camera_matrix_r.txt",np.float32)
print(camera_matrix_r)

dist_coeffs_l = np.loadtxt("CameraCalibrated/_dist_coeffs_l.txt",np.float32)
print(dist_coeffs_l)
dist_coeffs_r = np.loadtxt("CameraCalibrated/_dist_coeffs_r.txt",np.float32)
print(dist_coeffs_r)

#grayL = cv2.cvtColor(frameL,cv2.COLOR_BGR2GRAY);
#grayR = cv2.cvtColor(frameR,cv2.COLOR_BGR2GRAY);


mapL1 = np.loadtxt("CameraCalibrated/_mapL1.txt",np.float32)
print(mapL1)
mapL2 = np.loadtxt("CameraCalibrated/_mapL2.txt",np.float32)
print(mapL2)

mapR1 = np.loadtxt("CameraCalibrated/_mapR1.txt",np.float32)
print(mapR1)
mapR2 = np.loadtxt("CameraCalibrated/_mapR2.txt",np.float32)
print(mapR2)


print()
print("-> View ...")

keep_processing = True;

while (keep_processing):

    # grab frames from camera (to ensure best time sync.)

    camL.grab();
    camR.grab();

    # then retrieve the images in slow(er) time
    # (do not be tempted to use read() !)

    ret, frameL = camL.retrieve();
    ret, frameR = camR.retrieve();

    # undistort and rectify based on the mappings (could improve interpolation and image border settings here)

    undistorted_rectifiedL = cv2.remap(frameL, mapL1, mapL2, cv2.INTER_LINEAR);
    undistorted_rectifiedR = cv2.remap(frameR, mapR1, mapR2, cv2.INTER_LINEAR);

    # display image

    #cv2.imshow(windowNameL,undistorted_rectifiedL);
    #cv2.imshow(windowNameR,undistorted_rectifiedR);
    show_images(undistorted_rectifiedL,undistorted_rectifiedR)
    # start the event loop - essential

    key = cv2.waitKey(40) & 0xFF; # wait 40ms (i.e. 1000ms / 25 fps = 40 ms)

    # It can also be set to detect specific key strokes by recording which key is pressed

    # e.g. if user presses "x" then exit

    if (key == ord('c')):
        keep_processing = False;

#####################################################################

# STAGE 5: calculate stereo depth information

# uses a modified H. Hirschmuller algorithm [HH08] that differs (see opencv manual)

# parameters can be adjusted, current ones from [Hamilton / Breckon et al. 2013]

# FROM manual: stereoProcessor = cv2.StereoSGBM(numDisparities=128, SADWindowSize=21);

# From help(cv2): StereoBM_create(...)
#        StereoBM_create([, numDisparities[, blockSize]]) -> retval
#
#    StereoSGBM_create(...)
#        StereoSGBM_create(minDisparity, numDisparities, blockSize[, P1[, P2[,
# disp12MaxDiff[, preFilterCap[, uniquenessRatio[, speckleWindowSize[, speckleRange[, mode]]]]]]]]) -> retval

print()
print("-> Done.")

cv2.destroyAllWindows()