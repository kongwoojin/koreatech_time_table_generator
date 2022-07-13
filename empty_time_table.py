import pandas as pd


def empty_table():
    values = []

    for i in range(18):
        tmp = []
        for j in range(7):
            tmp.append("")
        values.append(tmp)

    columns = ['월', '화', '수', '목', '금', '토', '일']

    index = []
    for i in range(9):
        for j in ['A', 'B']:
            index.append("%02d%s" % (i + 1, j))

    df = pd.DataFrame(values, index=index, columns=columns)
    return df
