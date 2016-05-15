#!/usr/bin/env python
import logging
import logging.handlers
import argparse
import sys

LOG_FILENAME = "joule.log"
LOG_LEVEL = logging.INFO

parser = argparse.ArgumentParser(description="joule service")
parser.add_argument("-l", "--log", help="file to write log to (default '" + LOG_FILENAME + "')")

# If the log file is specified on the command line then override the default
args = parser.parse_args()
if args.log:
        LOG_FILENAME = args.log


logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
handler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="midnight", backupCount=3)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class MyLogger(object):
        def __init__(self, logger, level):
                """Needs a logger and a logger level."""
                self.logger = logger
                self.level = level

        def write(self, message):
                # Only log if there is a message (not just a new line)
                sys.__stdout__.write(message)
                if message.rstrip() != "":
                        self.logger.log(self.level, message.rstrip())

sys.stdout = MyLogger(logger, logging.INFO)
sys.stderr = MyLogger(logger, logging.ERROR)
