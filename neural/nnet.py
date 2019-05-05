#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

import dlib
import numpy
import tensorflow as tf

from scipy.spatial import distance
from skimage import io
from object_detection.utils import ops
from utils import label_map_util
from utils import visualization_utils

from PIL import Image 

#region Main

#region PersonComparison

class PersonComparison(object):
    def __init__(self):
        self.__shape_predictor = None
        self.__face_recognition = None
        self.__detector = None

        self.__comparisonPhoto = []
    
    @property
    def comparisonPhoto(self):
        return self.__comparisonPhoto

    def loadData(self):
        if os.path.exists('..\\neural_ready\\shape_predictor_68_face_landmarks.dat') and os.path.isfile('..\\neural_ready\\shape_predictor_68_face_landmarks.dat'):
            if os.path.exists('..\\neural_ready\\dlib_face_recognition_resnet_model_v1.dat') and os.path.isfile('..\\neural_ready\\dlib_face_recognition_resnet_model_v1.dat'):
                self.__shape_predictor = dlib.shape_predictor('..\\neural_ready\\shape_predictor_68_face_landmarks.dat')
                self.__face_recognition = dlib.face_recognition_model_v1('..\\neural_ready\\dlib_face_recognition_resnet_model_v1.dat')
                self.__detector = dlib.get_frontal_face_detector()
                return True
        return False
    
    def addPhoto(self, path):
        if os.path.exists(path) and os.path.isfile(path):
            image = io.imread(path)
            self.__comparisonPhoto.append(image)
            return True
        return False
    
    def determinePhoto(self, image):
        determinator = self.__detector(image)
        if not determinator:
            return [[0], False]
        print(determinator)
        for i_enum, j_enum in enumerate(determinator):
            print("Detection {}: LeftSide: {} TopSide: {} RightSide: {} BottomSide: {}".format(i_enum, j_enum.left(), j_enum.top(), j_enum.right(), j_enum.bottom()))
            shape = self.__shape_predictor(image, j_enum)
        return [self.__face_recognition.compute_face_descriptor(image, shape), True]

    def calculateDistance(self, dist_1, dist_2):
        return distance.euclidean(dist_1, dist_2)

#endregion

#region FindingObjects

class FindingObjects(object):
    def __init__(self):
        self.__model_graph = None
        self.__model_graph_def = None

        self.__label_map = None
        self.__categories = None
        self.__categories_dictionary = None

        # see more: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
        self.__finding_fast = '..\\neural_ready\\ssd_resnet50_v1_fpn_shared_box_predictor_640x640_coco14_sync_2018_07_03\\frozen_inference_graph.pb'
        self.__finding_normal = '..\\neural_ready\\faster_rcnn_inception_resnet_v2_atrous_coco_2018_01_28\\frozen_inference_graph.pb'
        self.__finding_slow = '..\\neural_ready\\faster_rcnn_nas_coco_2018_01_28\\frozen_inference_graph.pb'

    @property
    def finding_fast(self):
        return self.__finding_fast
    @property
    def finding_normal(self):
        return self.__finding_normal   
    @property
    def finding_slow(self):
        return self.__finding_slow

    def loadData(self, mode):
        self.__model_graph = tf.Graph()

        if os.path.exists('..\\neural_ready\\mscoco_label_map.pbtxt') and os.path.isfile('..\\neural_ready\\mscoco_label_map.pbtxt'):
            self.__label_map = label_map_util.load_labelmap('..\\neural_ready\\mscoco_label_map.pbtxt')
            
            self.__categories = label_map_util.convert_label_map_to_categories(self.__label_map, max_num_classes=100, use_display_name=True)
            self.__categories_dictionary = label_map_util.create_category_index(self.__categories)

            with self.__model_graph.as_default(): # pylint debug error? "context manager 'generator' doesn't implement __enter__ and __exit__" is not a true 
                self.__model_graph_def = tf.GraphDef()
                with tf.gfile.GFile(mode, 'rb') as file:
                    serialized = file.read()
                    self.__model_graph_def.ParseFromString(serialized)
                    tf.import_graph_def(self.__model_graph_def, name='')

            return True        
        return False
    
    def loadImage(self, path):
        if os.path.exists(path) and os.path.isfile(path):
            image = Image.open(path)
            (image_width, image_height) = image.size
            return numpy.array(image.getdata()).reshape((image_height, image_width, 3)).astype(numpy.uint8)

    def tensorboardDebug(self):
        with self.__model_graph.as_default(): # pylint debug error? "context manager 'generator' doesn't implement __enter__ and __exit__" is not a true
            with tf.Session() as current_session:
                tf.summary.FileWriter('log_simple_graph', current_session.graph)

    def process(self, processed_image):
        with self.__model_graph.as_default(): # pylint debug error? "context manager 'generator' doesn't implement __enter__ and __exit__" is not a true
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

                    detection_masks_reframed = ops.reframe_box_masks_to_image_masks(detection_masks, detection_boxes, 
                    processed_image.shape[0], processed_image.shape[1])
                    detection_masks_reframed = tf.cast(tf.greater(detection_masks_reframed, 0.5), tf.uint8)
                    tensorflow_dictionary['detection_masks'] = tf.expand_dims(detection_masks_reframed, 0)
                
                image_current_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

                tensorflow_output_dictionary = current_session.run(tensorflow_dictionary, feed_dict=
                {image_current_tensor: numpy.expand_dims(processed_image, 0)})

                tensorflow_output_dictionary['num_detections'] = int(tensorflow_output_dictionary['num_detections'][0])
                tensorflow_output_dictionary['detection_classes'] = tensorflow_output_dictionary['detection_classes'][0].astype(numpy.uint8)
                tensorflow_output_dictionary['detection_boxes'] = tensorflow_output_dictionary['detection_boxes'][0]
                tensorflow_output_dictionary['detection_scores'] = tensorflow_output_dictionary['detection_scores'][0]
                if 'detections_masks' in tensorflow_output_dictionary:
                    tensorflow_output_dictionary['detections_masks'] = tensorflow_output_dictionary['detections_masks'][0]
        
        visualization_utils.visualize_boxes_and_labels_on_image_array(
            processed_image,
            tensorflow_output_dictionary['detection_boxes'],
            tensorflow_output_dictionary['detection_classes'],
            tensorflow_output_dictionary['detection_scores'],
            self.__categories_dictionary,
            instance_masks=tensorflow_output_dictionary.get('detections_masks'),
            use_normalized_coordinates=True,
            line_thickness=3
        )

        return Image.fromarray(processed_image)
        
#endregion

#endregion