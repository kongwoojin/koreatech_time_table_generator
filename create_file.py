import os


def create_file():
    exclude_path = f"{os.getcwd()}/exclude_time.txt"

    if not os.path.exists(exclude_path):
        f = open(exclude_path, 'w', encoding="UTF-8")
        f.close()