"""
author: Jiayi Zhu
"""

from typing import Iterable, Union, Callable
from matplotlib import pyplot
from scipy import optimize
import numpy as np


def poly_fit_plot(x: Union[np.ndarray, Iterable, int, float],
                  y: Union[np.ndarray, Iterable, int, float],
                  mode: int,
                  deg: int = None,
                  func: Callable = None,
                  draw=True,
                  data_label: str = None,
                  fit_label: str = None,
                  pic_name='a.png'):
    """
    多项式拟合， 并画出原数据散点图与拟合曲线

    示例
    ----
    >>> x_ = np.array([1, 2, 3, 4, 5])
    >>> y_ = np.array([2, 4, 4, 5, 6])
    >>> c, r_squared = poly_fit_plot(x_, y_, deg=1,
    ... data_label='原数据',
    ... fit_label='拟合曲线',
    ... pic_name='一次拟合.png')

    :param x: 自变量
    :param y: 因变量
    :param mode: 值为 0 时，为多项式拟合；值为 1 时，为曲线拟合
    :param deg: 多项式次数，mode=0时必填
    :param func: 拟合的函数，mode=1时必填
    :param draw: 是否绘图
    :param data_label: 原数据标签
    :param fit_label: 拟合曲线标签
    :param pic_name: 保存的图片名
    :return: 多项式从高到低次幂系数，
             R方
    """
    if mode == 0:
        if deg is None:
            raise Exception("deg must be int")
        p = np.polyfit(x, y, deg)
        f = 0
        for i in range(deg + 1):
            it = np.power(x, deg - i)
            f += it * p[i]
    elif mode == 1:
        if func is None:
            raise Exception("func must be Callable")
        p, _ = optimize.curve_fit(func, x, y)
        f = func(x, p)
    else:
        raise Exception("mode must be 0 or 1")
    r_s = np.corrcoef(y, f)[0, 1]
    if draw:
        pyplot.rc('font', family='SimHei')
        pyplot.scatter(x, y, label=data_label)
        pyplot.plot(x, func, label=fit_label)
        pyplot.legend()
        pyplot.savefig(pic_name, dpi=500)
        pyplot.show()
    return p, r_s ** 2


if __name__ == '__main__':
    x_1 = np.array([0, 1, 2, 3, 4])
    y_1 = np.array([2, 4, 5, 8, 10])
    print(poly_fit_plot(x_1, y_1,
                        deg=1,
                        data_label='原数据',
                        fit_label='拟合曲线',
                        pic_name=r"C:\Users\ANO4679\Desktop\a.png"))
    pass
