import os
from read_excel import read_excel
from empty_time_table import empty_table
from create_directory import create_directory
from copy import deepcopy

count_of_time_table = 0


def clean_output():
    path = f"{os.getcwd()}/output/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith("placeholder"):
            continue
        os.remove(path + file)
    print("Output cleaning finished!")


def get_next_time(class_time):
    num = int(class_time[0:2])
    alphabet = class_time[2:]
    if alphabet == "A":
        alphabet = "B"
    elif alphabet == "B":
        num += 1
        alphabet = "A"
    return "%02d%s" % (num, alphabet)


def add_time_table(init_time_table, class_data, num):
    global count_of_time_table
    for name, value in class_data[num].items():
        for day_and_time in value:
            is_success = True
            times = day_and_time.split(',')
            time_table = deepcopy(init_time_table)
            now_time_table = deepcopy(time_table)

            is_conflict = False
            for time in times:
                class_day = time[0:1]
                class_start, class_end = time[1:].split('~')
                class_time = class_start

                while True:
                    if time_table[class_day][class_time] != "":
                        is_conflict = True
                        break
                    time_table[class_day][class_time] = name
                    if class_time == class_end:
                        break
                    class_time = get_next_time(class_time)
                if is_conflict:
                    is_success = False
                    break
                else:
                    now_time_table = deepcopy(time_table)

            if is_success:
                if num + 1 < len(class_data):
                    add_time_table(now_time_table, class_data, num + 1)
                else:
                    count_of_time_table += 1
                    print(f"{count_of_time_table}.xlsx generated!")
                    now_time_table.to_excel(f"output/{count_of_time_table}.xlsx")


def generate_time_table():
    create_directory()
    clean_output()
    add_time_table(empty_table(), read_excel(), 0)
    if count_of_time_table == 0:
        print("Can't generate timetable!")
    else:
        print(f"{count_of_time_table} timetable generated!")


if __name__ == "__main__":
    generate_time_table()