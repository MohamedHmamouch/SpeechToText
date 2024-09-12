from dataclasses import dataclass

@dataclass 
class DataIngestionArtifacts:

    download_data_path:str
    extracted_data_path:str


@dataclass
class DataPreprocessingArtifacts:
    train_data_path:str
    test_data_path:str

@dataclass
class ModelTrainerArtifacts:

    model_path:str
    model_loss:int