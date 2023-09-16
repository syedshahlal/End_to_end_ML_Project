from setuptools import setup, find_packages
from typing import List

PROJECT_NAME='housing-predictor'
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
        return requirements_file.readlines().remove("-e .")


setup(
    name=PROJECT_NAME,
    setup_requires=['setuptools_scm'],  # Add this line
    use_scm_version=True,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
