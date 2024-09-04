ARTIFACTS_DIR:str='artifacts'
PIPELINE_NAME:str='stt'

DATA_BUCKET_URI:str="s3://speech-to-text-project/data/"

#common files names
METADATA_DIR:str="metadata"
METADATA_FILE_NAME:str="metadata.csv"
WAVS_FILE_PATH:str='wavs.csv'

TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"


#ingestion data
DATA_DIR_NAME:str='data'
DOWNLOAD_DIR:str="download_data"
ZIP_FILE_NAME:str='LJSpeech-1.1.zip'
UNZIPPED_FOLDER_NAME:str="LJSpeech-1.1"


# Data preprocessing
DATA_PREPROCESSING_ARTIFACTS_DIR="data_preprocessing_artifacts"
DATA_PREPROCESSING_TRAIN_DIR="train"
DATA_PREPROCESSING_TEST_DIR="test"
TRAIN_TEST_SPLIT_RATIO=0.99
MAX_TARGET_LENGTH=5
