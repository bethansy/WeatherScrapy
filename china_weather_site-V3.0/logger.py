#!/usr/local/Python3.6.4/bin/python
# -*- coding: utf-8 -*-
import logging
import datetime
import os
import config

def getLogger(scriptname):
    logger = logging.getLogger(scriptname)
    logger.setLevel(logging.DEBUG)
    dateStr = datetime.datetime.now().strftime('%Y-%m')
    if not logger.handlers:
        logFile = config.logFilePath + scriptname + "_" + dateStr + ".log"
        filehandler = logging.FileHandler(logFile)
        filehandler.setLevel(logging.DEBUG)

        consolehandler = logging.StreamHandler()
        consolehandler.setLevel(logging.ERROR)

        formatter = logging.Formatter("%(asctime)s - %(filename)s - %(module)s - %(levelname)s - %(message)s")
        filehandler.setFormatter(formatter)
        consolehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        logger.addHandler(consolehandler)

    logger.info("\n\n" + "==" * 50 + "\n" + os.path.join(os.path.dirname(__file__), scriptname) + "\n" + "--" * 50)
    return logger