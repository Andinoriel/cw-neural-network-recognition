#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# using TensorFlow Object Detection API
# see more: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md
#           https://medium.com/@rohitrpatil/how-to-use-tensorflow-object-detection-api-on-windows-102ec8097699
#
# using COCO dataset via TensorFlow Detection Model Zoo 
# see more: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
#
# aviable datasets: 
#   - faster_rcnn_nas_coco_2018_01_28
#       specs:
#           speed: 1833ms (on nVidia Titan X via tensorflow-gpu)
#           COCO mAP[^1]: 43
#           folder size: 1.19GB
#   - faster_rcnn_inception_resnet_v2_atrous_coco_2018_01_28
#       specs:
#           speed: 620ms (on nVidia Titan X via tensorflow-gpu)
#           COCO mAP[^1]: 37
#           folder size: 711MB
#   - ssd_resnet50_v1_fpn_shared_box_predictor_640x640_coco14_sync_2018_07_03
#       specs:
#           speed: 76ms (on nVidia Titan X via tensorflow-gpu)
#           COCO mAP[^1]: 35
#           folder size: 385MB
#
#   current: faster_rcnn_nas_coco_2018_01_28
#

import sys
import threading

import numpy
import tensorflow as tf
from object_detection.utils import ops
from utils import label_map_util
from utils import visualization_utils

from PIL import Image

check = True

def main(): 
    # loading COCO faster_rcnn_nas
    model_graph = tf.Graph()
    with model_graph.as_default():
        model_graph_def = tf.GraphDef()
        with tf.gfile.GFile('..\\neural_ready\\faster_rcnn_nas_coco_2018_01_28\\frozen_inference_graph.pb', 'rb') as file:
            serialized = file.read()
            model_graph_def.ParseFromString(serialized)
            tf.import_graph_def(model_graph_def, name='')

    # loading category labels
    label_map = label_map_util.load_labelmap('..\\neural_ready\\mscoco_label_map.pbtxt')
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=100, use_display_name=True)
    categories_dictionary = label_map_util.create_category_index(categories)

    # loading image
    image = Image.open('image_tests\\broadway.jpg')
    (image_width, image_height) = image.size
    processed_image = numpy.array(image.getdata()).reshape((image_height, image_width, 3)).astype(numpy.uint8)

    # working with tensorflow ready model on session
    with model_graph.as_default():
        with tf.Session() as current_session:
            ops = tf.get_default_graph().get_operations()
            all_aviable_tensors_name = {output.name for op in ops for output in op.outputs}
            tensorflow_dictionary = {}
            for key in [
                'num_detections', 'detection_boxes', 'detection_scores',
                'detection_classes', 'detection_masks'
            ]:
                current_tensor_name = key + ':0'
                if current_tensor_name in all_aviable_tensors_name:
                    tensorflow_dictionary[key] = tf.get_default_graph().get_tensor_by_name(current_tensor_name)
            if 'detections_masks' in tensorflow_dictionary:
                detection_boxes = tf.squeeze(tensorflow_dictionary['detection_boxes'], [0])
                detection_masks = tf.squeeze(tensorflow_dictionary['detection_masks'], [0])
                num_detections = tf.cast(tensorflow_dictionary['num_detections'], tf.int32)

                detection_boxes = tf.slice(detection_boxes, [0, 0], [num_detections, -1])
                detection_masks = tf.slice(detection_masks, [0, 0, 0], [num_detections, -1, -1])

                detection_masks_reframed = ops.reframe_box_masks_to_image_masks(detection_masks, detection_boxes, 
                    processed_image.shape[0], processed_image.shape[1])
                detection_masks_reframed = tf.cast(tf.greater(detection_masks_reframed, 0.5), tf.uint8)
                tensorflow_dictionary['detection_masks'] = tf.expand_dims(detection_masks_reframed, 0)

            image_current_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

            # starting finding objects
            tensorflow_output_dictionary = current_session.run(tensorflow_dictionary, feed_dict=
                {image_current_tensor: numpy.expand_dims(processed_image, 0)})
            
            # transormation data
            tensorflow_output_dictionary['num_detections'] = int(tensorflow_output_dictionary['num_detections'][0])
            tensorflow_output_dictionary['detection_classes'] = tensorflow_output_dictionary['detection_classes'][0].astype(numpy.uint8)
            tensorflow_output_dictionary['detection_boxes'] = tensorflow_output_dictionary['detection_boxes'][0]
            tensorflow_output_dictionary['detection_scores'] = tensorflow_output_dictionary['detection_scores'][0]
            if 'detections_masks' in tensorflow_output_dictionary:
                tensorflow_output_dictionary['detections_masks'] = tensorflow_output_dictionary['detections_masks'][0]

            # tensorflow_output_dictionary contains information about the objects found and their parameters 
    
    # visualization
    visualization_utils.visualize_boxes_and_labels_on_image_array(
        processed_image,
        tensorflow_output_dictionary['detection_boxes'],
        tensorflow_output_dictionary['detection_classes'],
        tensorflow_output_dictionary['detection_scores'],
        categories_dictionary,
        instance_masks=tensorflow_output_dictionary.get('detections_masks'),
        use_normalized_coordinates=True,
        line_thickness=3
    )

    # displaying image
    output = Image.fromarray(processed_image)
    output.save('image_tests\\output.jpg')

    print('ending...')
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
