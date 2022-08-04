"""
author: Jiayi Zhu
"""
from scipy.sparse.linalg import eigs
from scipy.linalg import eig, eigvals
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


def mat_cr(mat_a: np.ndarray):
    """
    计算一致性比率

    输入判断矩阵的阶数应在 3~15 之间
    :param mat_a: 输入矩阵
    :return:
    """
    l_a, _ = eigs(mat_a, 1)
    len_ = len(mat_a)
    if 15 >= len_ > 2:
        cr_a = (l_a - len_)/(len_ - 1)/RI[len_ - 1]
    else:
        raise NotImplemented
    return np.real(cr_a)[0]


def max_lambda(mat_a: np.ndarray):
    """
    计算最大特征值

    """
    lambda_ = np.real(eig(mat_a)[0])
    return np.max(lambda_)


def weight_vec(mat_a: np.ndarray):
    """
    .. math:: AX = \\lambda_{max} X

    将 X 归一化作为权向量 W

    :param mat_a: 输入矩阵
    :return: 返回 W
    """
    lambda_ = np.real(eig(mat_a)[0])
    vec_ = eig(mat_a)[1].T
    v = []
    for i in range(len(lambda_)):
        if lambda_[i] == np.max(lambda_):
            v = vec_[i]
    return np.real(v/sum(v))


if __name__ == '__main__':

    # print(l_a_)
    # print(len(d))
    # print(mat_cr(d))
    m = np.array([[1, 3], [1/3, 1]])
    l_ = eig(m)
    print(l_[0])
    print(weight_vec(m))



