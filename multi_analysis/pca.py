"""
author: Jiayi Zhu
主成分分析
"""
import numpy
from sklearn import decomposition


class PCA:
    def __init__(self, data_, n_: int):
        """
        输入训练数据和指标维度

        示例
        -----
        >>> data = [[2, 3, 4],
        ...         [3, 6, 9],
        ...         [7, 2, 8],
        ...         [1, 5, 0]]
        >>> md = PCA(data, 3)

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

    def print_ratio(self):
        """

        :return: 打印主成分的贡献率
        """
        print(self._ratio_)

    def get_principals(self, rate=0.8):
        """
        得到主成分总贡献率大于 rate 的前 k 个主成分

        一般 rate 取 0.8 或 0.85

        示例
        ----
        >>> data = [[2, 3, 4],
        ...         [3, 6, 9],
        ...         [7, 2, 8],
        ...         [1, 5, 0]]
        >>> md = PCA(data, 3)
        >>> md.print_ratio()
        [0.78144882 0.19448163 0.02406956]

        >>> print(md.get_principals(0.8))
        [[ -4.09863867  -8.581568   -10.10172591   0.08339598]
         [  2.6722813    6.31058992   0.77637815   3.05140146]]

        :param rate: 前 k 个主成分总贡献率应达到的比率
        :return: 前 k 个主成分
        """
        principals = []
        sum_r = 0.0
        n = 0
        for i in range(len(self._ratio_)):
            sum_r += self._ratio_[i]
            if sum_r >= rate:
                n = i + 1
                break
        for m in range(n):
            p = []
            for line in self._data_:
                s = 0.0
                for i in range(self._n_):
                    s += line[i] * self._coe_[m][i]
                p.append(s)
            principals.append(p)
        return numpy.array(principals)

    def get_coe(self, n: int = None):
        """
        第 n 个主成分的系数，若 n 为 None，返回所有主成分的系数

        注意
        ----
        n 从 0 开始计数

        示例
        ----
        >>> data = [[2, 3, 4],
        ...         [3, 6, 9],
        ...         [7, 2, 8],
        ...         [1, 5, 0]]
        >>> md = PCA(data, 3)
        >>> print(md.get_coe(1)) # 返回第二个主成分的系数
        [-0.55975349  0.72223099  0.40627383]

        """
        if n is None:
            return self._coe_
        else:
            return self._coe_[n]


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
    print(f.get_principals(0.8))
