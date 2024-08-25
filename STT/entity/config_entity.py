import os
from STT.constants import *

from datetime import datetime

from dataclasses import dataclass

TIMESTAMP:str=datetime.now().strftime('m_%d_%Y_%H_%M_%S')

ROOT=os.getcwd()

@dataclass
class TrainingPipelineConfig:

    pipeline_name:str=PIPELINE_NAME
    artifact_dir:str=os.path.join(ROOT,ARTIFACTS_DIR,TIMESTAMP)
    timestamp:str=TIMESTAMP

training_pipeline_config:TrainingPipelineConfig=TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    bucket_uri=DATA_BUCKET_URI
    file_name=ZIP_FILE_NAME
    download_dir=os.path.join(ROOT,DATA_DIR_NAME,DOWNLOAD_DIR)
    s3_zip_file_path:str=os.path.join(download_dir,file_name)
    unzip_data_dir_path:str=os.path.join(ROOT,DATA_DIR_NAME)