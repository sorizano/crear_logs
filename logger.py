import logging
import streamlit as st

@st.cache_resource
def setup_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)

    return logger

# Creación de los loggers
activity_logger = setup_logger("activity", "logs/activity.log", logging.INFO)
warning_logger = setup_logger("warning", "logs/warning.log", logging.WARNING)
error_logger = setup_logger("error", "logs/error.log", logging.ERROR)