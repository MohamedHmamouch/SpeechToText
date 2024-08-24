import logging
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_DIR_PATH = os.path.join(os.getcwd(), LOG_DIR)

os.makedirs(LOG_DIR, exist_ok=True)

CURRENT_TIME_STAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"log_{CURRENT_TIME_STAMP}.log"
log_file_path = os.path.join(LOG_DIR, file_name)

logging.basicConfig(
    level=logging.INFO,
    filename=log_file_path,
    format="%(asctime)s %(levelname)s %(module)s =====> %(message)s",
    datefmt="%d-%m-%Y %H:%M"
)

logger = logging.getLogger()
