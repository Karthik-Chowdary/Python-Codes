import os
import string
def rename_files():

    file_list = os.listdir(r"/Users/KarthikChowdary/Desktop/prank");
    print(file_list);
    saved_path = os.getcwd()
    os.chdir(r"/Users/KarthikChowdary/Desktop/prank");
    remove_digits = str.maketrans('', '', "0123456789")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(remove_digits))
    os.chdir(saved_path);
rename_files()
