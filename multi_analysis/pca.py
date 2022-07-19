from sklearn.decomposition import PCA


def analyze(data_, n_: int):
    module_ = PCA(n_components=n_)
    module_.fit(data_)
    print('特征值为:', module_.explained_variance_)
    print('各主成分的贡献率:', module_.explained_variance_ratio_)
    print('奇异值为:', module_.singular_values_)
    print('各主成分的系数:\n', module_.components_)



if __name__ == '__main__':
    arr = [[149.5, 69.5, 38.5],
           [162.5,   77, 55.5],
           [162.7, 78.5, 50.8],
           [162.2, 87.5, 65.5],
           [156.5, 74.5, 49.0]]

    analyze(arr, 3)



