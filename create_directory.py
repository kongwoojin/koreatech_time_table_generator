import os


def create_directory():
    output_path = f"{os.getcwd()}/output/"
    excel_path = f"{os.getcwd()}/excel/"

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    if not os.path.exists(excel_path):
        os.makedirs(excel_path)
