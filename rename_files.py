import os
import re

def rename_files():

    file_list=os.listdir(r"E:\Courses\Programming Foundations - Python\Photos")

    for file_name in file_list:
        os.rename(file_name,re.sub("^[0-9]+","",file_name))
        print(file_name)
rename_files()
