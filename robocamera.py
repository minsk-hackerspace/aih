import cv2
import numpy as np

class RoboCamera:
    def __init__(self,left_device,right_device):
        self.camera_matrix_l = np.loadtxt("CameraCalibrated/_camera_matrix_l.txt",np.float32)
        self.camera_matrix_r = np.loadtxt("CameraCalibrated/_camera_matrix_r.txt",np.float32)
        self.dist_coeffs_l = np.loadtxt("CameraCalibrated/_dist_coeffs_l.txt",np.float32)
        self.dist_coeffs_r = np.loadtxt("CameraCalibrated/_dist_coeffs_r.txt",np.float32)
        self.mapL1 = np.loadtxt("CameraCalibrated/_mapL1.txt",np.float32)
        self.mapL2 = np.loadtxt("CameraCalibrated/_mapL2.txt",np.float32)

        self.mapR1 = np.loadtxt("CameraCalibrated/_mapR1.txt",np.float32)
        self.mapR2 = np.loadtxt("CameraCalibrated/_mapR2.txt",np.float32)
        self.capture_l=cv2.VideoCapture(left_device)
        self.capture_r=cv2.VideoCapture(right_device)

    def get_undistorted_images(self):
        self.capture_l.grab()
        self.capture_r.grab()
        
        retL, frameL = self.capture_l.retrieve()
        retR, frameR = self.capture_r.retrieve()

        if(not(retR and retL)):
            return None

        undistorted_rectifiedL = cv2.remap(frameL, self.mapL1, self.mapL2,cv2.INTER_LINEAR)
        undistorted_rectifiedR = cv2.remap(frameR, self.mapR1, self.mapR2,cv2.INTER_LINEAR)

        return (undistorted_rectifiedL,undistorted_rectifiedR)


    def pair_to_3d(point2d_l,point2d_r):
        '''Takes point in the left and right image. Returns point in 3d. 
        Uses camera matrix, etc.'''
        displacement = point2d_l.x-point2d_l.y
        camera_matrix = self.camera_matrix_l
        f_x=camera_matrix[0,0]
        f_y=camera_matrix[1,1]
        z=

        return np.array([0.5,0.5,0.5,1])
        

