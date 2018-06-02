import os
import re

def rename_files():
    
    curr_dir = os.getcwd();
    file_list=os.listdir(r"E:\Courses\Programming Foundations - Python\Photos")
    os.chdir("E:\Courses\Programming Foundations - Python\Photos");

    for file_name in file_list:
        os.rename(file_name,re.sub("^[0-9]+","",file_name))

    os.chdir(curr_dir)
rename_files()
