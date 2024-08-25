import sys
import os
from STT.exceptions import STTException
from STT.logger import logging
from STT.entity.config_entity import DataIngestionConfig
from STT.entity.artifacts_entity import DataIngestionArtifacts
from STT.constants import *
from STT.cloud_storage.s3_operations import S3Sync
from zipfile import ZipFile


class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):

        try:

            self.data_ingestion_config=data_ingestion_config
            self.s3_sync=S3Sync()

        except Exception as e:

            raise STTException(e,sys)
        
    
    def get_data_from_cloud(self)->None:

        try:

            logging.info('Initiating data download from s3 bucket')

            download_dir=self.data_ingestion_config.download_dir
            bucket_dir=self.data_ingestion_config.bucket_uri

            s3_zip_file_path=self.data_ingestion_config.s3_zip_file_path

            if os.path.isdir(download_dir):

                logging.info(
                    f"data is already present in {download_dir} so skipping download step"
                )

                return None
            
            else:

                os.makedirs(download_dir,exist_ok=True)
                self.s3_sync.sync_folder_from_s3(download_dir,bucket_dir)
                logging.info(f"data is downloaded from s3 bucket in directory {download_dir}")

        except Exception as e:

            raise STTException(e,sys)
        
    def unzip_data(self)->None:

        try:

            logging.info("Unzipping the download zip file from download directory")

            s3_zip_file_path=self.data_ingestion_config.s3_zip_file_path
            unzip_data_dir_path=self.data_ingestion_config.unzip_data_dir_path
            unzip_data_dir=os.path.join(unzip_data_dir_path,UNZIPPED_FOLDER_NAME)
            if os.path.isdir(unzip_data_dir):

                logging.info('Unzipped folder already exists in unizp directory')

            else:

                os.makedirs(unzip_data_dir,exist_ok=True)
                with ZipFile(s3_zip_file_path,"r") as zip_file_ref:

                    zip_file_ref.extractall(unzip_data_dir_path)

        except Exception as e:

            raise STTException(e,sys)
        
    def initiate_data_ingestion(self)->DataIngestionArtifacts:

        try: 
            logging.info('Initiating the data ingestion component')
            self.get_data_from_cloud()
            self.unzip_data()

            exctrated_data_path=os.path.join(self.data_ingestion_config.unzip_data_dir_path,UNZIPPED_FOLDER_NAME)

            data_ingestion_artifat=DataIngestionArtifacts(
                download_data_path=self.data_ingestion_config.download_dir,
                extracted_data_path=exctrated_data_path
            )

            logging.info('data ingestion is completed successfully')


            return data_ingestion_artifat
        
        except Exception as e:

            raise STTException(e,sys)
        

