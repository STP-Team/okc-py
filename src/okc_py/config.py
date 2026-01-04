"""Configuration settings for OKC API wrapper."""

import logging
import sys

from pydantic_settings import BaseSettings, SettingsConfigDict


def setup_logging(log_level: str = "INFO"):
    """Configure standard logging for the okc_py package.

    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    level = getattr(logging, log_level.upper(), logging.INFO)

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stderr,
    )


class Settings(BaseSettings):
    """OKC API configuration settings."""

    # OKC API Configuration
    BASE_URL: str = "https://okc.ertelecom.ru/yii"

    # Request Configuration
    REQUEST_TIMEOUT: int = 30
    MAX_RETRIES: int = 3
    RETRY_DELAY: float = 1.0

    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = True
    REQUESTS_PER_SECOND: float = 5.0

    # Logging
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True, extra="ignore"
    )
