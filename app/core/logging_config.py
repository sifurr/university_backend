import logging
import logging.config
import os


# ensure logs directory exists
os.makedirs("logs", exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "default": {
            "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        },
    },

    "handlers": {
        
        #console output
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },

        # General app log
        "file": {
            "class": "logging.FileHandler",
            "filename": "logs/app.log",
            "formatter": "default",
            "level": "INFO"
        },

        # Error specifig log
        "error_file": {
            "class": "logging.FileHandler",
            "filename": "logs/error.log",
            "formatter": "default",
            "level": "ERROR",
        },
    },

    "root": {
        "handlers": ["console", "file", "error_file"],
        "level": "INFO",
    },
}


def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)




