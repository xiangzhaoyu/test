#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 下午5:05
# @Author  : zhaoyu
# @Site    : 
# @File    : test_keras.py
# @Software: PyCharm


# from keras.models import Sequential
# from keras.layers import Concatenate, Input, Dense

import numpy as np
import cv2
import keras.backend as K
import tensorflow as tf


# a = Input((100, 300))
# b = Input((100, 200))
# c = Concatenate(axis=-1)([a, b])
# print(c)


kenel_size = (3,)
input_dim = 30
filters = 12
a = kenel_size + (input_dim, filters)
print(a)

t1 = K.variable(np.array([[[1, 2], [2, 3]], [[4, 4], [5, 3]]]))
t2 = K.variable(np.array([[[7, 4], [8, 4]], [[2, 10], [15, 11]]]))
d0 = K.concatenate([t1, t2], axis=-2)
d1 = K.concatenate([t1, t2], axis=1)
d2 = K.concatenate([t1, t2], axis=-1)
d3 = K.concatenate([t1, t2], axis=2)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(d0))
    print(sess.run(d1))
    print(sess.run(d2))
    print(sess.run(d3))