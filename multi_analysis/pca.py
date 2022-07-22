"""
author: Jiayi Zhu
主成分分析
"""
import numpy
from sklearn import decomposition


class PCA:
    def __init__(self, data_, n_: int):
        """
        示例
        -------
        >>> data = [[2, 3, 4], [3, 6, 9]]
        >>> md = PCA(data)

        :param data_: array_like
        :param n_: dimensions
        """
        self._data_ = data_
        self._n_ = n_
        module_ = decomposition.PCA(n_components=self._n_)
        module_.fit(self._data_)

        self._eigen_ = module_.explained_variance_
        self._ratio_ = module_.explained_variance_ratio_
        self._singular_ = module_.singular_values_
        self._coe_ = module_.components_

    def print_all(self):
        """
        特征值

        各主成分的贡献率

        奇异值

        各主成分的系数

        """
        print('特征值为:', self._eigen_)
        print('各主成分的贡献率:', self._ratio_)
        print('奇异值为:', self._singular_)
        print('各主成分的系数:\n', self._coe_)

    def get_principals(self, n: int):
        """

        :param n: 主成分的个数
        :return: 前 n 个主成分
        """
        principals = []
        for m in range(n):
            p = []
            for line in self._data_:
                s = 0.0
                for i in range(self._n_):
                    s += line[i] * self._coe_[m][i]
                p.append(s)
            principals.append(p)
        return principals


if __name__ == '__main__':
    arr = [
        [149.5, 69.5, 38.5],
        [162.5, 77.0, 55.5],
        [162.7, 78.5, 50.8],
        [162.2, 87.5, 65.5],
        [156.5, 74.5, 49.0],
        [156.1, 74.5, 45.5],
        [172.0, 76.5, 51.0],
        [173.2, 81.5, 59.5],
        [159.5, 74.5, 43.5],
        [157.7, 79.0, 53.5]
    ]

    npa = numpy.array(arr)
    f = PCA(npa, 3)
    f.print_all()
    print(f.get_principals(1))
