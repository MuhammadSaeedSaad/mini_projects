import os

def rename_files():
    # (1) get file names from a folder
    file_names = os.listdir(r"/home/kali/Desktop/dev/small_projects/RenameFiles/prank")
    print(file_names)
    saved_path = os.getcwd()
    print("current working directory "+saved_path)
    os.chdir(r"/home/kali/Desktop/dev/small_projects/RenameFiles/prank")
    
    # (2) rename the files
    for file_name in file_names:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    
    os.chdir(saved_path)

rename_files()
print("hello")
