from setuptools import setup
from typing import List

PROJECT_NAME='housing-predictor'
VERSION='0.0.1'
AUTHOR='Syed Shahlal'
DESCRIPTION='This is a simple housing price predictor app'
PACKAGES=['housing']
REQUIREMENTS_FILE_PATH='requirements.txt'


def get_requirements_list()->List[str]:
    """
    Description: This function returns the list of requirements from requirements.txt file

    Returns: This function returns the list which contains the packages/libraries name from requirements.txt file
    """
    with open(REQUIREMENTS_FILE_PATH,'r') as requirements_file:
        return requirements_file.readlines()


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)