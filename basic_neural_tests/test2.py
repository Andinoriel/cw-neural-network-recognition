import sys
import threading

import dlib
from scipy.spatial import distance
from skimage import io

check = True

def main():
        # shape_predictor - ready neuralnet for face recognition
        # face_recognition - ready model data using 68 face keypoints
        shape_predictor = dlib.shape_predictor('neural_ready\\shape_predictor_68_face_landmarks.dat')
        face_recognition = dlib.face_recognition_model_v1('neural_ready\\dlib_face_recognition_resnet_model_v1.dat')
        detector = dlib.get_frontal_face_detector()

        # loading first image
        image_1 = io.imread('image_tests\\image1.jpg')
        image_rec_1 = dlib.image_window()
        image_rec_1.clear_overlay()
        image_rec_1.set_image(image_1)

        # loading second image
        image_2 = io.imread('image_tests\\image2.jpg')
        image_rec_2 = dlib.image_window()
        image_rec_2.clear_overlay()
        image_rec_2.set_image(image_2)


        #determinate first image data
        determinators1 = detector(image_1, 1)
        #determinate second image data
        determinators2 = detector(image_2, 1)

        # finding keypoints via shape_predictor & face_recognition for the first image
        for i,j in enumerate(determinators1):
                print("Detection {}: LeftSide: {} TopSide: {} RightSide: {} BottomSide: {}".format(i, j.left(), j.top(), j.right(), j.bottom()))
                shape = shape_predictor(image_1, j)
                image_rec_1.clear_overlay()
                image_rec_1.add_overlay(j)
                image_rec_1.add_overlay(shape)

        image_descriptor_1 = face_recognition.compute_face_descriptor(image_1, shape)
        
        # finding keypoints via shape_predictor & face_recognition for the second image
        for i,j in enumerate(determinators2):
                print("Detection {}: LeftSide: {} TopSide: {} RightSide: {} BottomSide: {}".format(i, j.left(), j.top(), j.right(), j.bottom()))
                shape = shape_predictor(image_2, j)
                image_rec_2.clear_overlay()
                image_rec_2.add_overlay(j)
                image_rec_2.add_overlay(shape)

        image_descriptor_2 = face_recognition.compute_face_descriptor(image_2, shape)

        # finding euclidean distance to compare the images
        descriptor_check = distance.euclidean(image_descriptor_1, image_descriptor_2)
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
        main = threading.Thread(target=main)
        chckIntrpt = threading.Thread(target=checkInterrupt)
        main.start()
        chckIntrpt.start()
else:
        pass