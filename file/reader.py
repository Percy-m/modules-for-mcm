# unnecessary
import pandas
import numpy
import datetime as dt


def read_csv(path_, header_=0, sep_=',', use_cols_=None):
    """

    :param path_:
    :param header_:
    :param sep_:
    :param use_cols_:
    :return: numpy Ndarray
    """
    data_ = pandas.read_csv(path_, sep=sep_, header=header_, usecols=use_cols_)
    return data_


if __name__ == '__main__':
    # path = r"C:\Users\ANO4679\..Temp\data.csv"
    # d0 = read_csv(path)
    # d = pandas.read_csv(path, usecols=range(1, 2))
    # npa = numpy.array(d)
    # print(d0)
    # print(d)
    # print(npa)

    p1 = r"C:\Users\ANO4679\Desktop\A.xlsx"
    data = pandas.read_excel(p1, sheet_name='Sheet1')
    print(data)
    print(data.values)
    v = data.values
    for line in v:
        print()


