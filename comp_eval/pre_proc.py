import math

import numpy as np

# 指标的一致化处理


def small_to_large(indicator_: np.ndarray):
    """
    极小型指标化为极大型指标

    Example
    -------
    >>> s = np.array([1, 3, 5, 7])
    >>> small_to_large(s)
    [6 4 2 0]
    """
    return np.max(indicator_) - indicator_


def middle_to_large(indicator_: np.ndarray):
    """
    居中型指标化为极大型指标

    Example
    -------
    >>> m = np.array([1, 4, 5, 7, 9])
    >>> middle_to_large(m)
    [0.   0.75 1.   0.5  0.  ]
    """
    max_ = np.max(indicator_)
    min_ = np.min(indicator_)
    res_ = []
    for e in indicator_:
        if e <= (max_ + min_) / 2:
            res_.append(2 * (e - min_) / (max_ - min_))
        else:
            res_.append(2 * (max_ - e) / (max_ - min_))
    return np.array(res_)


def interval_to_large(indicator_: np.ndarray, lb_: float, ub_: float):
    """
    区间型指标化为极大型指标

    Example
    -------
    >>> i = np.array([2, 5, 6, 10, 13])
    >>> interval_to_large(i, 5, 9)
    [0.25 1.   1.   0.75 0.  ]

    :param indicator_: 指标
    :param lb_: 区间下界
    :param ub_: 区间上界
    """
    max_ = np.max(indicator_)
    min_ = np.min(indicator_)
    c_ = np.amax([lb_ - min_, max_ - ub_])
    res_ = []
    for e in indicator_:
        if e < lb_:
            res_.append(1 - (lb_ - e)/c_)
        elif e > ub_:
            res_.append(1 - (e - ub_)/c_)
        else:
            res_.append(1.0)
    return np.array(res_)


# 指标的无量纲化处理


def std_trans(indicator_: np.ndarray):
    """
    标准样本变换法
    """
    mu_ = np.mean(indicator_)
    return (indicator_ - mu_)/indicator_.std()


def range_trans(indicator_: np.ndarray):
    """
    极差变换法（适用于极大型指标）
    """
    max_ = np.max(indicator_)
    min_ = np.min(indicator_)
    return (indicator_ - min_)/(max_ - min_)


if __name__ == '__main__':
    ap = np.array([2, 3, 4, 9, 10, 13])
    print(small_to_large(ap))
    print(middle_to_large(ap))
    print(interval_to_large(ap, 5, 9))
    print(std_trans(ap))
    print(range_trans(ap))
