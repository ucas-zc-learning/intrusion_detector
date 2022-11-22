# !/usr/bin/python3
from model import *


if __name__ == '__main__':
    _M_model = model()
    _M_model.start("Gaussian Naive Bayes Model", gnb)
    _M_model.start("Decision Tree Classifier Model", dtc)
    _M_model.start("Random Forest Model", rfst)
    _M_model.start("Support Vector Classifier", svc)
