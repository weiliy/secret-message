import os

def rename_files():
    #(1) get file names form a folder
    file_list = os.listdir(r"./prank/")

    #(2) for each file, rename filename
    saved_path = os.getcwd()
    os.chdir(r"./prank/")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
