import os

# Create a folder
dir = os.getcwd()

target_folder = os.path.join(dir, 'housing')

# print(target_folder)

create_folders = ['exception','logger','pipeline', 'component','config','entity','utils', ]
for folder in create_folders:
    path = os.path.join(target_folder, folder)
    # print(path)
    if not os.path.exists(path):  # Check if the path does not exist
        os.mkdir(path)
        with open(os.path.join(path, '__init__.py'), 'w') as f:
            pass
