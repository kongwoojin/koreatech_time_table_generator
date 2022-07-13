import os
import pandas as pd


def read_excel():
    class_data = []

    path = f"{os.getcwd()}/excel/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith("placeholder") or file.startswith("#"):
            continue
        file_path = path + file
        df = pd.read_excel(file_path, sheet_name=0, usecols=[4, 11])
        now_class = df.loc[0][0]
        tmp = {now_class: []}
        for i in range(len(df)):
            time = df.loc[i][1]
            if time not in tmp[now_class]:
                tmp[now_class].append(time)
        class_data.append(tmp)

    exclude_path = f"{os.getcwd()}/exclude_time.txt"
    if os.stat(exclude_path).st_size != 0:
        f = open(exclude_path, 'r', encoding="UTF-8")
        lines = f.readlines()
        tmp = []
        for line in lines:
            tmp.append(line.strip())

        class_data.append({'공강': [",".join(tmp)]})
        f.close()

    return class_data
