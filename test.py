import sys
from STT.exceptions import STTException
from STT.logger import logging
logging.info('test')
try:

    print(1/0)


except Exception as e:

    raise STTException(e,sys)