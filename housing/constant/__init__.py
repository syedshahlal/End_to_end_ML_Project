import os

from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


ROOT_DIR = os.getcwd()
TARGET_FOLDER = os.path.join(ROOT_DIR, 'housing')
CREATE_FOLDERS = ['exception', 'logger', 'pipeline', 'component', 'config', 'entity', 'utils', 'constant']
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)
CURRENT_TIME_STAMP = get_current_time_stamp()

# Training pipeline related constants
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"