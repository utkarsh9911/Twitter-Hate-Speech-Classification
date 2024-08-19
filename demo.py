from hate_speech.exception import CustomException
import sys
from hate_speech.logger import logging


try:
    a = 7 / 0
except Exception as e:
    raise CustomException(e, sys) from e


