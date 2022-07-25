"""
author: Jiayi Zhu
"""

from typing import Iterable, Union
from matplotlib import pyplot
import numpy as np


def poly_fit_plot(x: Union[np.ndarray, Iterable, int, float],
                  y: Union[np.ndarray, Iterable, int, float],
                  degree: int,
                  pic_name='a.png'):
    """
    多项式拟合， 并画出原数据散点图与拟合曲线
    :param x:
    :param y:
    :param degree:
    :param pic_name:
    :return:
    """
    p = np.polyfit(x, y, degree)
    pyplot.scatter(x, y)
    func = 0
    for i in range(degree + 1):
        it = np.power(x, degree - i)
        func += it * p[i]
    pyplot.plot(x, func)
    pyplot.savefig(pic_name, dpi=500)
    pyplot.show()
    return p


if __name__ == '__main__':
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 4, 5, 6])
    print(poly_fit_plot(x, y, 1))
