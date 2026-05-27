# number 8 logger created after creating html and allure report
import logging
import os
class LogGen:

    @staticmethod
    def loggen():

        project_path = os.getcwd()

        log_path = os.path.join(
            project_path,
            "logs",
            "automation.log"
        )

        logger = logging.getLogger("automation")

        logger.setLevel(logging.INFO)

        if not logger.handlers:

            file_handler = logging.FileHandler(log_path)

            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s'
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger