import os
import logging

class Logger:
    @staticmethod
    def get_logger():
        log_dir = 'C:\\Users\\moham\\PycharmProjects\\Heruko_Project\\logs'
        log_file_path = os.path.join(log_dir, 'test_log.log')

        # Create the logs directory if it doesn't exist
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger

    @staticmethod
    def info(message):
        logger = Logger.get_logger()
        logger.info(message)