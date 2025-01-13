import os

def list_files_in_directory(directory):
    return os.listdir(directory)

print(list_files_in_directory('.'))
print(os.system('systeminfo'))