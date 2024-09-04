import os
import sys
import csv
from glob import glob

from STT.entity.config_entity import DataIngestionConfig,DataPreprocessingConfig
from STT.entity.artifacts_entity import DataPreprocessingArtifacts,DataIngestionArtifacts
from STT.models.data_utils import VectorizerChar,get_data
from STT.logger import logging
from STT.exceptions import STTException
from STT.constants import *

class DataPreprocessing:

    def __init__(self,
                 data_preprocessing_config:DataPreprocessingConfig,
                 data_ingestion_artifacts:DataIngestionArtifacts):
        
        try:

            self.data_preprocessing_config=data_preprocessing_config
            self.data_ingestion_artifact=data_ingestion_artifacts

        except Exception as e:
            raise STTException(e,sys)
        
    
    def get_id_to_text(self)->tuple:

        try:

            logging.info('Entering the get id to index method of DataPreprocessing')

            os.makedirs(self.data_preprocessing_config.data_preprocessig_artifact_dir,exist_ok=True)

            metadata=os.path.join(self.data_ingestion_artifact.extracted_data_path,METADATA_FILE_NAME)
            
            waves_path=self.data_ingestion_artifact.extracted_data_path
            wavs=None
            logging.info("writing the path wavs")
            self.wavs=glob("{}/**/*.wav".format(waves_path),recursive=True)

            logging.info("creating the dictionary to id to text")

            self.id_to_text={}

            with open(metadata,encoding="utf-8") as f:

                for line in f:

                    id=line.strip().split('|')[0]
                    text=line.strip().split('|')[2]
                    self.id_to_text[id]=text

            os.makedirs(self.data_preprocessing_config.metadata_dir_path,exist_ok=True)

            with open(self.data_preprocessing_config.wavs_file_path,"w") as f:

                write=csv.writer()
                write.writerows(self.wavs)

            logging.info("Existing the get_id_to_index method fo data preprocessing")

            return self.wavs,self.id_to_text
        except Exception as e:

            raise STTException(e,sys)
        
    def extract_data(self)->None:

        try:

            logging.info('Entering the extract_data method of preprocessing')

            self.data=get_data(self.wavs,self.id_to_text,maxlen=MAX_TARGET_LENGTH)

            logging.info("Existing the extract_data method of preprocessing")

        except Exception as e:

            raise STTException(e,sys)
        
    def train_test_split(self)->tuple:

        try:

            logging.info('Entering the train test split method of preprocessing')

            split=int(len(self.data))*TRAIN_TEST_SPLIT_RATIO
            train_data=self.data[:split]
            test_data=self.data[split:]

            logging.info('writing train data')
            os.makedirs(self.data_preprocessing_config.train_dir_path,exist_ok=True)

            keys=train_data[0].keys()
            self.train_file_path=os.path.join(self.data_preprocessing_config.train_dir_path,TRAIN_FILE_NAME)


            with open(self.train_file_path,'w',newline='') as output_file:

                dict_writer=csv.DictWriter(output_file,keys)
                dict_writer.writeheader()
                dict_writer.writerows(train_data)

            logging.info('write test data')
            os.makedirs(self.data_preprocessing_config.test_dir_path,exist_ok=True)

            self.test_file_path=os.path.join(self.data_preprocessing_config.test_dir_path,TEST_FILE_NAME)
            with open(self.test_file_path,'w',newline='') as output_file:

                dict_writer=csv.DictWriter(output_file,keys)
                dict_writer.writeheader()
                dict_writer.writerows(test_data)
                output_file.close()

            logging.info('train test split of the data is done')
            return train_data,test_data
        
        except Exception as e:

            raise STTException(e,sys)
        

    def initiate_data_preprocessing(self):

        try:
            logging.info('initiate data preprocessing')
            self.get_id_to_text()
            self.extract_data()
            self.train_test_split()

            data_preprocessing_artifact=DataPreprocessingArtifacts(
                train_data_path=self.train_file_path,
                test_data_path=self.test_file_path
            )

            logging.info('Data Preprocessing completed successuflly')

            return data_preprocessing_artifact
        
        except Exception as e:

            raise STTException(e,sys)
        

        
            

