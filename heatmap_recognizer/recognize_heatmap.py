import tensorflow as tf
import pandas as pd
import numpy as np

from detector import Detector
from util import load_image

import skimage.io
import matplotlib.pyplot as plt

import os
#import ipdb
import sys


label_dict_path = '../../results/mytech/label_dict.pickle'

weight_path = '../../caffe_layers_value.pickle'
model_path = '../../models/mytech'

batch_size = 1

label_dict = pd.read_pickle( label_dict_path )
n_labels = len( label_dict )

images_tf = tf.placeholder( tf.float32, [None, 224, 224, 3], name="images")
labels_tf = tf.placeholder( tf.int64, [None], name='labels')

detector = Detector( weight_path, n_labels )
c1,c2,c3,c4,conv5, conv6, gap, output = detector.inference( images_tf )
classmap = detector.get_classmap( labels_tf, conv6 )

sess = tf.InteractiveSession()
saver = tf.train.Saver()

saver.restore( sess, tf.train.latest_checkpoint(model_path) )


current_images = np.array(map(lambda x: load_image(x), sys.argv[1:]))
current_image_paths = sys.argv[1:]

good_index = np.array(map(lambda x: x is not None, current_images))

current_image_paths = [ x for x,y in zip(current_image_paths,good_index) if y]

current_images = np.stack(current_images[good_index])

conv6_val, output_val = sess.run(
            [conv6, output],
            feed_dict={
                images_tf: current_images
                })

label_predictions = output_val.argmax( axis=1 )

classmap_vals = sess.run(
            classmap,
            feed_dict={
                labels_tf: label_predictions,
                conv6: conv6_val
                })


classmap_vis = map(lambda x: ((x-x.min())/(x.max()-x.min())), classmap_vals)
rev_label_dict={}
for x in label_dict.keys():
    rev_label_dict[label_dict[x]]=x

label_names = [rev_label_dict[x] for x in label_predictions] 
for img_name,label_name in zip(current_image_paths,label_names):
    print img_name,":",label_name

for vis, ori,ori_path, l_name in zip(classmap_vis, current_images, current_image_paths, label_names):
        print l_name

        vis_path = '/tmp/results/'+ ori_path.split('/')[-1]
        vis_path_ori = '/tmp/results/'+ori_path.split('/')[-1].split('.')[0]+'.ori.jpg'
        skimage.io.imsave( vis_path, vis )
        skimage.io.imsave( vis_path_ori, ori )

