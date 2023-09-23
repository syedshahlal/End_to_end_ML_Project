import yaml
from housing.exception import HousingException
from housing.constant import *
import os, sys

def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e


def create_folders_in_dir(TARGET_FOLDER: str, CREATE_FOLDERS: list) -> None:
    """
    Create folders in the target folder and add __init__.py if it doesn't exist.
    
    Args:
    TARGET_FOLDER (str): The target folder in which to create subfolders.
    CREATE_FOLDERS (list): A list of subfolder names to be created.
    """
    try:
        for folder in CREATE_FOLDERS:
            path = os.path.join(TARGET_FOLDER, folder)
            if not os.path.exists(path):
                os.mkdir(path)
            
            init_file = os.path.join(path, '__init__.py')
            if not os.path.exists(init_file):
                with open(init_file, 'w') as f:
                    pass
    except Exception as e:
        raise HousingException(e,sys) from e
    
def update_version(file_path='version.txt'):
    """
    Update the version number stored in a file.

    Args:
    file_path (str): The path to the file containing the version number. Defaults to 'version.txt'.

    Returns:
    str: The new version number after updating.
    """
    def read_version():
        """
        Read the current version number from the file.

        Returns:
        str: The current version number as a string.
        """
        try:
            with open(file_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return "0.0.0"

    current_version = read_version()

    major, minor, patch = map(int, current_version.split('.'))
    patch += 1
    new_version = f"{major}.{minor}.{patch}"

    with open(file_path, 'w') as file:
        file.write(new_version)

    return new_version