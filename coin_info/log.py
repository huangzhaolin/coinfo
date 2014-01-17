__author__ = 'zhaolinhuang'
import os
import logging
import traceback
from logging.handlers import  TimedRotatingFileHandler

LOG_DIR="/Users/zhaolinhuang/logs/coinfo"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

log=logging.getLogger("COINFO")
logging.basicConfig(level=logging.INFO)
fileTimeHandler=TimedRotatingFileHandler("%s/common.log"%LOG_DIR,"D",1)
fileTimeHandler.setFormatter(logging.Formatter("%(asctime)s : %(message)s"))
fileTimeHandler.suffix="%Y-%m-%d.log"
log.addHandler(fileTimeHandler)