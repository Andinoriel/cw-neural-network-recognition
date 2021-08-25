import os
import dlib

from scipy.spatial import distance
from skimage import io

import pkg_resources


class Facecomp(object):
    def __init__(self, threshold=0.6):
        self.__threshold = threshold
        self.__faces = []

        self.__load()

    def __load(self) -> None:
        self.__predictor = dlib.shape_predictor(pkg_resources.resource_filename(
            "models", "shape_predictor_68_face_landmarks.dat"))
        self.__recognitor = dlib.face_recognition_model_v1(pkg_resources.resource_filename(
            "models", "dlib_face_recognition_resnet_model_v1.dat"))
        self.__detector = dlib.get_frontal_face_detector()

    def __determine(self, face) -> list:
        determinator = self.__detector(face)

        if not determinator:
            return [[0], False]

        for _, j in enumerate(determinator):
            print(f"left: {j.left()} top: {j.top()} "
                  f"right: {j.right()} bottom: {j.bottom()}")
            shape = self.__predictor(face, j)

        return [self.__recognitor.compute_face_descriptor(face, shape), True]

    def add_faces(self, face1, face2) -> bool:
        if (os.path.exists(face1) and os.path.isfile(face1) and
                os.path.exists(face2) and os.path.isfile(face2)):
            self.__faces.clear()

            self.__faces.append(io.imread(face1))
            self.__faces.append(io.imread(face2))

            return True
        return False

    def compare(self) -> bool:
        delta1, is_valid1 = self.__determine(self.__faces[0])
        delta2, is_valid2 = self.__determine(self.__faces[-1])

        return (True if (is_valid1 and is_valid2 and
                         distance.euclidean(delta1, delta2) < self.__threshold)
                else False)

