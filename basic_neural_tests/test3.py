# using TensorFlow Object Detection API
# see more: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md
#           https://medium.com/@rohitrpatil/how-to-use-tensorflow-object-detection-api-on-windows-102ec8097699

# using COCO dataset via TensorFlow Detection Model Zoo (see more: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md)
# current dataset: faster_rcnn_nas
# specs:
#       speed: 1833ms (on nVidia Titan X via tensorflow-gpu)
#       COCO mAP[^1]: 43
#       folder size: 1.19GB

import sys
import threading

import numpy
import tensorflow as tf
import tensorflow_object_detection.research.object_detection.utils as ut
from matplotlib import pyplot
from PIL import Image

check = True

def main():

    global check
    while check == True:
        pass


def checkInterrupt():
    global check
    input()
    check = False

if __name__ == '__main__':
    current = threading.Thread(target=main)
    chckIntrpt = threading.Thread(target=checkInterrupt)
    current.start()
    chckIntrpt.start()
else:
    pass
