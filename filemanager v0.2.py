import os
import shutil
def file_manage():
    def get_all_files(extension):
        files = []
        for fetch_files in os.listdir("."):
            if fetch_files.endswith(extension):
                files.append(fetch_files)
        return files

    input_extension = input("Enter The Extension(like .exe) :")
    all_files = get_all_files(input_extension)
    total_files = len(all_files)
    folder_name = input_extension+" Files"
    if total_files > 0:
        os.mkdir(folder_name)
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

