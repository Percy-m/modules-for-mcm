"""
author: Jiayi Zhu
"""
import numpy as np
from sklearn.linear_model import LinearRegression


class MultiVariableLinear:

    def __init__(self, data_x, data_y):
        self._model = LinearRegression()
        self._model.fit(data_x, data_y)

    pass
