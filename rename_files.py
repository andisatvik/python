import os

def rename_files():

    file_list=os.listdir(r"E:\Courses\Programming Foundations - Python\Photos")

    for file_name in file_list:
        print(file_name)

rename_files()
