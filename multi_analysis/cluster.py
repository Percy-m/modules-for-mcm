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
from sklearn import preprocessing as _pp
import scipy.cluster.hierarchy as _sch
import matplotlib.pyplot as _plt


# def hiera_cluster(
#         data: np.ndarray
# ):
#
#     pass


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
    print(d)
    print(mat_d)
    print(z)
    s = np.array([str(i+1) for i in range(7)])
    _plt.rc('font', size=16)
    _sch.dendrogram(z, labels=s)
    _plt.show()
