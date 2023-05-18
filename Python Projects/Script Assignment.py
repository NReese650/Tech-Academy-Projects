import os

def check_text_files(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            modified_time = os.path.getmtime(file_path)
            print("File: {} | Modified Time: {}".format(file_name, modified_time))

# Specify the folder path to check for text files
folder_path = r"C:\Script_Assignment"

# Call the function to check text files in the specified folder
check_text_files(folder_path)
