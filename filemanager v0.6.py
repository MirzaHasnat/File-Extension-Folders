import os
import shutil
def file_manage():
    def get_all_files(extension):
        files = []
        for fetch_files in os.listdir("."):
            if fetch_files.endswith(extension):
                files.append(fetch_files)
        return files
    
    #asking For Extension From Users
    input_extension = input("Enter The Extension(like .exe if(you want to move multiple extension in 1 folder then all extension seprate by commas)) :").split(",")
    
    #getting All files like input_extension
    all_files = get_all_files(tuple(input_extension))
    
    #length of total files like input_extension
    total_files = len(all_files)
    #asking For Folder Name
    ask_for_folder_name = input("Enter Folder Name :")

    #if extension are more than 1
    if len(input_extension) >1:
        
        #if folder name is empty
        if ask_for_folder_name == "":
            folder_name = "Multiple Files"
        else:
            folder_name = ask_for_folder_name
    else:
        #if Folder Name is Empty
        if ask_for_folder_name == "":
            folder_name = input_extension+" Files"
        else:
            folder_name = ask_for_folder_name
            
    if total_files > 0:
        #if folder is already exist
        if os.path.isdir(folder_name):
            print("Folder Already Exist")
        else:
            os.mkdir(folder_name)
        # Moving The Files Process Start Here 
        for move_file in range(total_files):
            shutil.move(all_files[move_file],folder_name)
            print(all_files[move_file]+" DONE!")
    else:
        print("No File Found")


question = input("If you Have More File Type to Manage(y/n) :")
while True:
    if question=="y":
        file_manage()
    else:
        print("bye")
        exit()

