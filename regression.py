# -*- coding: utf-8 -*-
"""Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i1SYocWaodiQzl0d24kpudeeV5Ixn_tx
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 100

Lr = 0.00001 #learning rate
data_set = {"office_size": np.random.normal(320, 60, n)}
data_set["office_price"] = np.random.normal(5000, 60, n)

pd.DataFrame(data_set)

class LinearRegression:
  def __init__(self, size, Lr):
    self.n_weight = 0
    self.n_bias = 0
    self.data_size = size
    self.Lr = Lr
    self.sum_error_squared = 0

  def predict(self, weight, bias, data_set):
    y_predict = data_set["office_size"] * weight + bias
    return y_predict

  def mean_squared_error(self, data_set):
    data_set["error"] = data_set["office_price"] - data_set["y_predict"]
    data_set["error_squared"] = data_set["error"]**2
    return sum(data_set['error_squared'])/self.data_size

  def gradient_descent(self, bias, weight):
    self.n_bias = bias - (self.Lr * - 2 * sum (data_set["error"]))
    self.n_weight = weight - (self.Lr * ((-2/self.data_size) * sum(data_set["office_size"] * data_set["error"])))
    return self.n_bias, self.n_weight

model = LinearRegression(n, Lr)

weight = 0.6
bias = 6
epochs = 100

for i in range(epochs):
  data_set["y_predict"] = model.predict(weight, bias, data_set)

  model.mean_squared_error(data_set)

  bias, weight = model.gradient_descent(bias, weight)


pd.DataFrame(data_set)

weight, bias

plt.scatter(data_set["office_size"], data_set["y_predict"])
plt.plot(data_set["office_size"], data_set["y_predict"], "yellow")

size = 100
price = weight * size + bias
price