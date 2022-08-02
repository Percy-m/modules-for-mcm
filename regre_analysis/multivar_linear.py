"""
author: Jiayi Zhu
"""
import numpy as np
from sklearn.linear_model import LinearRegression


class MultiVariableLinear:

    def __init__(self, data_x, data_y):
        self.data_x = data_x
        self.data_y = data_y
        model = LinearRegression().fit(self.data_x, self.data_y)

    pass
