import sys
import cv2
import re
import numpy
import numpy.ma as ma
import math
from os.path import basename
import matplotlib.pylab as plt
import matplotlib.gridspec as grd



def otsu(hist):
  def safediv(x,y):
    if y == 0:
      return 0
    else:
      return float(x)/float(y)
  totalleft = reduce(lambda x,y: x+[x[-1]+y], hist, [0,])
  total = totalleft[-1]
  totalright = map (lambda x: total -x ,totalleft)

  weighted = [ i*hist[i] for i in range(len(hist))]
  sumweightedleft = reduce(lambda x,y: x+[x[-1]+y], weighted, [0,])
  sumweighted = sumweightedleft[-1]
  sumweightedright = map(lambda x: sumweighted -x, sumweightedleft)

  Wb = map(lambda x: float(x)/float(total), totalleft)
  Wf = map(lambda x: float(x)/float(total), totalright)
  Mb = [ safediv(sumweightedleft[i],totalleft[i]) for i in range(len(totalleft))]
  Mf = [ safediv(sumweightedright[i],totalright[i]) for i in range(len(totalright))]
  sigma2 = [ Wb[i]*Wf[i]*(Mb[i]-Mf[i])**2 for i in range(len(Wb))]
  return sigma2.index(max(sigma2))


def between(x,a,b):
    if x>=a and x<=b:
        return numpy.uint8(255)
    else:
        return numpy.uint8(0)

def threshold_hsv(im,img_class):
    hsv_dict={'apple':{
        'minh': 27, 
        'maxh': 54,
        'mins': 13,
        'maxs': 222,
        'minv':0,
        'maxv': 255
        }
        }
    im_hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    b1=numpy.vectorize(lambda x: between(x,hsv_dict[img_class]['minh'],hsv_dict[img_class]['maxh']))
    b2=numpy.vectorize(lambda x: between(x,hsv_dict[img_class]['mins'],hsv_dict[img_class]['maxs']))
    b3=numpy.vectorize(lambda x: between(x,hsv_dict[img_class]['minv'],hsv_dict[img_class]['maxv']))
    proc_im_h=b1(im_hsv[:,:,0])
    proc_im_s=b2(im_hsv[:,:,1])
    proc_im_v=b3(im_hsv[:,:,2])
    proc_im=cv2.bitwise_and(proc_im_h,cv2.bitwise_and(proc_im_s,proc_im_v))
    return proc_im

def threshold_difference(im,img_class):
    coeff_dict={
            'apple':{'r':0.0,'g':1.0,'b':0.0, 't':100}
            }
    def positive_part(x):
        if(x>0):
            return x
        else:
            return 0
    ppart=numpy.vectorize(positive_part)
    proc_im = im[:,:,0]*coeff_dict[img_class]['b']+ im[:,:,1]*coeff_dict[img_class]['g']+ im[:,:,2]*coeff_dict[img_class]['r']
    proc_im2=ppart(proc_im).astype('uint8')
    res,proc_im = cv2.threshold(proc_im2,coeff_dict[img_class]['t'],255,cv2.THRESH_BINARY)
    if res:
        return proc_im
    else:
        return None




im = cv2.imread(sys.argv[1])
imname = basename(sys.argv[1])

im_proc1 = threshold_hsv(im,sys.argv[2])


def find_min_rect(labels,idx):
    #print contours
    rect=cv2.minAreaRect(find_contour(labels,idx))
    #print rect
    return rect

def process_connected_components(img):
    print "Finding connected components"
    res,labels,stats,centroids=cv2.connectedComponentsWithStats(img)
    def aspect_ratio(x):
        minlen = min(stats[x][cv2.CC_STAT_HEIGHT],stats[x][cv2.CC_STAT_WIDTH])
        maxlen = max(stats[x][cv2.CC_STAT_HEIGHT],stats[x][cv2.CC_STAT_WIDTH])
        if minlen==0:
            minlen=1
        return float(maxlen)/float(minlen)



    idxs=range(len(centroids))
    idxs = filter(lambda x: stats[x][cv2.CC_STAT_AREA]<200*200,idxs)
    idxs = filter(lambda x: stats[x][cv2.CC_STAT_AREA]>10*10,idxs)
    idxs = filter(lambda x: stats[x][cv2.CC_STAT_HEIGHT]<300,idxs)
    idxs = filter(lambda x: stats[x][cv2.CC_STAT_WIDTH]<300,idxs)
    idxs = filter (lambda x: aspect_ratio(x)<2.0,idxs)


    for idx in range(len(centroids)):
        if idx not in idxs:
            labels[labels==idx]=0
    
    for idx in idxs:
        print centroids[idx]

    show_img = img.copy()
    res_centroids = [centroids[idx] for idx in idxs]
    #for idx in idxs:
    #    cv2.circle(show_img,tuple(centroids[idx].astype('uint16')),10,(0,0,255))
    #return show_img
    return res_centroids


res_centroids=process_connected_components(im_proc1)

for centroid in res_centroids:
    cv2.circle(im,tuple(centroid.astype('uint16')),10,(0,0,255))
    

cv2.imwrite('/tmp/res'+imname+'.jpg',im)
