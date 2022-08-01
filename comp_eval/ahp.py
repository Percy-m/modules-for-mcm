"""
author: Jiayi Zhu
"""
from scipy.sparse.linalg import eigs
import numpy as np

CR = [
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
    l_a, v_a = eigs(mat_a, 1)
    len_ = len(mat_a)
    if len_ > 2:
        cr_a = (l_a - len_)/len_ - 1/CR[len_]
    else:
        cr_a = 0
    return cr_a


if __name__ == '__main__':
    pass
