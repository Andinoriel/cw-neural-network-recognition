#!/usr/bin/env python3

# thx to https://github.com/davisking and his repo
# with ready models: https://github.com/davisking/dlib-models

import urllib.request
import bz2


def get(url, path):
    file, _ = urllib.request.urlretrieve(url)
    data = bz2.BZ2File(file).read()
    open(path, "wb").write(data)


if __name__ == "__main__":
    get("https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2",
        "src/models/shape_predictor_68_face_landmarks.dat")
    get("https://github.com/davisking/dlib-models/raw/master/dlib_face_recognition_resnet_model_v1.dat.bz2",
        "src/models/dlib_face_recognition_resnet_model_v1.dat")
