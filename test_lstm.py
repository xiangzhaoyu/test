#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 下午4:16
# @Author  : zhaoyu
# @Site    : 
# @File    : test_lstm.py
# @Software: PyCharm

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from numpy import array
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.utils import plot_model

if __name__ == '__main__':
    length = 5
    seq = array([i / float(length) for i in range(length)])
    X = seq.reshape(len(seq), 1, 1)
    Y = seq.reshape(len(seq), 1)

    n_neurons = length
    n_batch = length
    n_epoch = 1000

    model = Sequential()
    model.add(LSTM(n_neurons, input_shape=(1, 1)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    print(model.summary())

    model.fit(X, Y, epochs=n_epoch, batch_size=n_batch, verbose=2)
    result = model.predict(X, batch_size=n_batch, verbose=0)
    for value in result:
        print('%.1f' % value)

    plot_model(model, to_file='lstm.png')