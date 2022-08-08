"""
author: Jiayi Zhu

层次聚类法：
（1）将每个样品独自聚成一类，构造 n 个类
（2）根据所确定的样品距离公式，计算 n 个样品（或变量）两两间的距离，构造距离矩阵 D_0
（3）把距离最近的两类归为一个新类，其他样品仍各自聚为一类，共聚成 n-1 类
（4）计算新类与当前各类的距离，将距离最近的两个类进一步聚成一类，共聚成 n-2 类。以上步骤一直进行下去，最后将所有样品聚成一类
（5）画聚类谱系图
（6）决定类的个数及包含各类的样品数，并对类做出解释
"""


import numpy as np
from numpy import ndarray
from sklearn import preprocessing as _pp
import scipy.cluster.hierarchy as _sch
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage
import matplotlib.pyplot as _plt


def hiera_cluster(data: ndarray,
                  method='single',
                  labels: ndarray = None,
                  pic_path='a.png'):
    """
    层次聚类，两两对象间的距离采用欧式距离，同时绘制聚类图

    method 可选参数有：

    'single' 最短距离法（默认）
    'average' 无权平均距离
    'centroid' 重心距离
    'complete' 最大距离
    'ward' 离差平方和方法

    :param data: 输入的数据
    :param method: 使用的方法
    :param labels: 聚类图横轴的标签，默认为0, 1, 2, ...
    :param pic_path: 聚类图保存路径
    :return: 矩阵格式的两两对象间距离 和 linkage后的聚类结果
    """
    format_data = _pp.minmax_scale(data)
    dist = pdist(format_data)
    mat_dist = squareform(dist)
    lk = linkage(d, method=method)
    _plt.rc('font', family='SimHei')
    _sch.dendrogram(lk, labels=labels)
    _plt.savefig(pic_path)
    _plt.show()
    return mat_dist, lk


if __name__ == '__main__':
    data_ = np.array([
        [2.9909, 0.3111, 0.5324],
        [3.2044, 0.5348, 0.7718],
        [2.8392, 0.5696, 0.7614],
        [2.5315, 0.4528, 0.4893],
        [2.5897, 0.3010, 0.2735],
        [2.9600, 2.0480, 1.4997],
        [3.1184, 2.8395, 1.9850]
    ])
    f_data = _pp.minmax_scale(data_)
    d = _sch.distance.pdist(f_data)
    mat_d = _sch.distance.squareform(d)
    z = _sch.linkage(d)

    print(f_data)
    print()
    print(d)
    print()
    print(mat_d)
    print()
    print(z)
    s = np.array([1, 2, 3, 4, 5, 6, 7])
    _plt.rc('font')
    _sch.dendrogram(z, labels=s)
    _plt.show()

    hiera_cluster(data_, 'complete', labels=s)
