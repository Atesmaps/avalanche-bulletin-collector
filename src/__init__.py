import logging
from pathlib import Path
from logging.config import fileConfig


logging_file = Path(__file__).resolve().parent / "logging.conf"
fileConfig(logging_file)

logger = logging.getLogger(__name__)
