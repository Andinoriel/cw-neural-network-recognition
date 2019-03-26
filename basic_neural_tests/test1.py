#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#   Recognition of handwritten numbers - TEST №1
#   see more: http://yann.lecun.com/exdb/mnist/
#   
#   using libraries:
#       numpy
#       TensorFlow
#       Keras
#

import sys

import tensorflow as tf  # machine learning
from keras.models import Sequential  # linear stack of layers
from keras.utils import np_utils  # different utils

import numpy # different math; arrays; matrix; very productive
from keras.layers import Dense # neuro: activation func etc; FEEDFORWARD NEURALNETWWORK

# stochastic optimization setting: current value for the data repeatability
numpy.random.seed(23)
# tensorflow mnist set of numbers data
mnist = tf.keras.datasets.mnist


def main():
    # DATA PREPROCESSING

    (x_training_set, y_training_set), (x_test_set, y_test_set) = mnist.load_data()
    x_training_set = x_training_set.reshape(60000, 784) # image's sizing reformation

    x_training_set = x_training_set.astype('float32') #data normalize
    x_training_set /= 255

    y_training_set = np_utils.to_categorical(y_training_set, 10) # transform neural output label into category - 10 digit
    # 0 --> [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # 1 --> [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    # 2 --> [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    # 3 --> [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    # 4 --> [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    # 5 --> [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    # 6 --> [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    # 7 --> [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    # 8 --> [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    # 9 --> [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    # NEURAL NETWORK 

    neural = Sequential() # creating feedforward neural

    # model type: Dense

    # input layer with 500 neuron each contains 784 input's; 
    # distribution: normal(Gaussian)
    # activation func: rectifier(ReLU); see more: https://en.wikipedia.org/wiki/Rectifier_(neural_networks)
    neural.add(Dense(500, input_dim=784, kernel_initializer='normal', activation='relu')) 

    # output layer with 10 neuron
    # distribution: normal(Gaussian)
    # activation func: softmax; see more:   
    neural.add(Dense(10, kernel_initializer='normal', activation='softmax'))

    # compiling neural
    # teaching method: SGD; see more: https://en.wikipedia.org/wiki/Stochastic_gradient_descent
    # measure of error: categorical_crossentropy ???
    # metrics optimization: accuracy
    neural.compile(loss='categorical_crossentropy', optimizer='SGD', metrics=['accuracy'])

    print(neural.summary())

    # MACHINE LEARNING

    # batching size - value using in stohastic gradient descent
    # neural epoch - how long to train on one data set
    # verbose - giving some technical information
    neural.fit(x_training_set, y_training_set, batch_size=100, nb_epoch=100, verbose=1)

    # ???
    # # setting predictions
    # predictions = neural.predict(x_training_set)
    # predictions = numpy.argmax(predictions, axis=1)

    scores = neural.evaluate(x_test_set, y_test_set, verbose=0)
    print('ACCURACY:%.3f%%' % (scores[1]*100))

if __name__ == '__main__':
    main()
    print('test #1 done...')
else:
    pass
