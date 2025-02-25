import logging
import os


def setup_logger(name, log_file, level=logging.INFO):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.Filehandler(log_file)
        handler.setFormatter(loggin.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)

     return logger

#Configuración de los loggers
activity_logger = setup_logger("activity", "logs/activity.log", logging.INFO)
warning_logger = setup_logger("warning", "logs/warning.log", logging.WARNING)
error_logger = setup_logger("error", "logs/error.log", logging.ERROR)