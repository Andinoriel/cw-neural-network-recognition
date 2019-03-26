#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import threading

import dlib
from scipy.spatial import distance
from skimage import io

check = True

def loadImg(path):
        read_img = io.imread(path)
        reco_img = dlib.image_window()
        reco_img.clear_overlay()
        reco_img.set_image(read_img)
        return [read_img, reco_img] 

def displayReco(predictor, read_img, reco_img, j):
        shape = predictor(read_img, j)
        reco_img.clear_overlay()
        reco_img.add_overlay(j)
        reco_img.add_overlay(shape)
        return shape

def main():
        # shape_predictor - ready neuralnet for face recognition
        # face_recognition - ready model data using 68 face keypoints
        shape_predictor = dlib.shape_predictor('neural_ready\\shape_predictor_68_face_landmarks.dat')
        face_recognition = dlib.face_recognition_model_v1('neural_ready\\dlib_face_recognition_resnet_model_v1.dat')
        detector = dlib.get_frontal_face_detector()

        # loading first image
        image_1, image_rec_1 = loadImg('image_tests\\image1.jpg')
        # loading second image
        image_2, image_rec_2 = loadImg('image_tests\\image3.jpg')

        #determinate first image data
        determinators1 = detector(image_1, 1)
        #determinate second image data
        determinators2 = detector(image_2, 1)

        # finding keypoints via shape_predictor & face_recognition for the first image
        for i,j in enumerate(determinators1):
                print("Detection {}: LeftSide: {} TopSide: {} RightSide: {} BottomSide: {}".format(i, j.left(), j.top(), j.right(), j.bottom()))
                shape = displayReco(shape_predictor, image_1, image_rec_1, j)
        image_descriptor_1 = face_recognition.compute_face_descriptor(image_1, shape)
        
        # finding keypoints via shape_predictor & face_recognition for the second image
        for i,j in enumerate(determinators2):
                print("Detection {}: LeftSide: {} TopSide: {} RightSide: {} BottomSide: {}".format(i, j.left(), j.top(), j.right(), j.bottom()))
                shape = displayReco(shape_predictor, image_2, image_rec_2, j)
        image_descriptor_2 = face_recognition.compute_face_descriptor(image_2, shape)

        # finding euclidean distance to compare the images
        descriptor_check = distance.euclidean(image_descriptor_1, image_descriptor_2)
        print(descriptor_check)
        if descriptor_check < 0.6:
                print('same human')
        else:
                print('not a same human')

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
