import os

DIR = os.getcwd()

def update_version():
    """
    Updates the version number stored in a 'version.txt' file by incrementing the patch version.

    If the 'version.txt' file does not exist, it initializes the version to '0.0.0' and then increments the patch version.

    The version is stored in the format 'major.minor.patch' where 'major' and 'minor' are integers, and 'patch' is incremented.

    After updating, the new version is printed, and the 'version.txt' file is updated with the new version.

    Example:
    - If the current version is '1.2.3', calling this function will update it to '1.2.4'.

    Usage:
    - Call this function to increment and update the version number in 'version.txt'.
    """

    # Read the current version from a file or initialize it if the file doesn't exist
    FILE_NAME = 'version.txt'
    FILE_PATH = os.path.join(DIR, FILE_NAME)
    try:
        with open(FILE_PATH, 'r') as file:
            current_version = file.read()
    except FileNotFoundError:
        current_version = "0.0.0"

    # Split the version string into its components (major, minor, patch)
    major, minor, patch = map(int, current_version.split('.'))

    # Increment the patch version
    patch += 1

    # Construct the new version string
    new_version = f"{major}.{minor}.{patch}"



    # Write the new version back to the file
    with open(FILE_PATH, 'w') as file:
        file.write(new_version)
    
        # Print the new version
    return(new_version)
