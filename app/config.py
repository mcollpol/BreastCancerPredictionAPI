"""
This module configures custom logging settings for the Breast Cancer Prediction API application.
It defines configuration settings using Pydantic BaseSettings and integrates the Loguru logging
library for enhanced logging capabilities.

Classes:
    LoggingSettings: Configuration settings for logging.
    Settings: Main settings configuration for the application.
    InterceptHandler: Custom logging handler to integrate with Loguru.
    
Functions:
    setup_app_logging(config: Settings): Configures application logging.
"""

import logging
import sys
from types import FrameType
from typing import List, cast

from loguru import logger
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class LoggingSettings(BaseSettings):
    """
    Configuration settings for logging.
    
    Attributes:
        LOGGING_LEVEL (int): The logging level. Default is logging.INFO.
    """
    LOGGING_LEVEL: int = logging.INFO  # logging levels are type int.


class Settings(BaseSettings):
    """
    Main settings configuration for the application.
    
    Attributes:
        API_V1_STR (str): The API version string.
        logging (LoggingSettings): Logging configuration settings.
        BACKEND_CORS_ORIGINS (List[AnyHttpUrl]): List of allowed CORS origins.
        PROJECT_NAME (str): The name of the project.
    """
    API_V1_STR: str = "/api/v1"

    logging: LoggingSettings = LoggingSettings()

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "https://localhost:3000",
        "https://localhost:8000",
    ]

    PROJECT_NAME: str = "Breast Cancer Prediction API"

    class Config:
        """
        Pydantic configuration for settings class.
        
        Attributes:
            case_sensitive (bool): Enable case sensitivity for environment variables.
        """
        case_sensitive = True


class InterceptHandler(logging.Handler):
    """
    Custom logging handler to integrate with Loguru.
    
    Methods:
        emit(record: logging.LogRecord): Emits a log record to Loguru.
    """
    def emit(self, record: logging.LogRecord) -> None:
        """
        Emit a log record to Loguru.
        
        Args:
            record (logging.LogRecord): The log record to emit.
        """
        # Get corresponding Loguru level if it exists.
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where the logged message originated.
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


def setup_app_logging(config: Settings) -> None:
    """
    Prepare custom logging for the application.
    
    This function configures the logging system to use Loguru for enhanced logging capabilities.
    
    Args:
        config (Settings): The application settings configuration.
    """
    loggers = ("uvicorn.asgi", "uvicorn.access")
    logging.getLogger().handlers = [InterceptHandler()]
    for logger_name in loggers:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level=config.logging.LOGGING_LEVEL)]

    logger.configure(
        handlers=[{"sink": sys.stderr, "level": config.logging.LOGGING_LEVEL}]
    )


settings = Settings()
