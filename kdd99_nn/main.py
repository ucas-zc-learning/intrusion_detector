# !/usr/bin/python3

from model import *


if __name__ == '__main__':
    _M_model = model()
    _M_model.start("shallow neural network", shallow_model)
    _M_model.start("deep neural network", deep_model)
    _M_model.start("convolutional neural network", cnn_model)