"""
author: Jiayi Zhu
"""
from scipy.sparse.linalg import eigs
import numpy as np

RI = [
    0,
    0,
    0.52,
    0.89,
    1.12,
    1.26,
    1.36,
    1.41,
    1.46,
    1.49,
    1.52,
    1.54,
    1.56,
    1.58,
    1.59
]


def mat_cr(mat_a):
    """
    计算一致性比率
    :param mat_a:
    :return:
    """
    l_a, _ = eigs(mat_a, 1)
    len_ = len(mat_a)
    if len_ > 2:
        cr_a = (l_a - len_)/len_ - 1/RI[len_]
    else:
        cr_a = 0
    return cr_a


def max_lambda(mat_a):
    _, v = eigs(mat_a, 1)
    return v


#

if __name__ == '__main__':
    a = [[1, 3, 4],
         [1/3, 1, 2],
         [1/4, 1/2, 1]]
    print(eigs(np.array(a), 1))

