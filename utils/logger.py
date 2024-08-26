import logging
import os

'''class Logger:
    @staticmethod
    def get_logger():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Create file handler for logging
        file_handler = logging.FileHandler('logs/test_log.log')
        file_handler.setLevel(logging.INFO)

        # Create formatter and add it to the handler
        file_handler = logging.FileHandler('logs/test_log.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        if not logger.hasHandlers():
            logger.addHandler(file_handler)

        return logger
# utils/logger.py
import os
import logging


class Logger:
    @staticmethod
    def get_logger():
        # Path to the logs directory
        log_dir = 'logs'

        # Ensure the log directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Path to the log file
        log_file_path = os.path.join(log_dir, 'test_log.log')

        # Create a logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Create a file handler for logging
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.INFO)

        # Create a formatter and add it to the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(file_handler)
        return logger
'''


class Logger:
    @staticmethod
    def get_logger():
        # Path to the logs directory
        log_dir = r'C:\Users\local_\PycharmProjects\Web_Automation_Framework\logs'

        # Ensure the log directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Path to the log file
        log_file_path = os.path.join(log_dir, 'test_log.log')

        # Create a logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Create a file handler for logging
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.INFO)

        # Create a formatter and add it to the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(file_handler)
        return logger

    @staticmethod
    def info(message):
        logger = Logger.get_logger()
        logger.info(message)
