import sys
import os
from STT.exceptions import STTException
from STT.logger import logging
from STT.entity.config_entity import DataIngestionConfig
from STT.entity.artifacts_entity import DataIngestionArtifacts
from STT.constants import *
from STT.cloud_storage.s3_operations import S3Sync
from zipfile import ZipFile