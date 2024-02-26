#!/usr/bin/env python3
###########################################
#
#   Pyrene - Avalanche Bulletin Collector
#
#   February 2024 - Atesmaps
#
###########################################
import logging

from src.pyrene.pyrene import Pyrene
from src.utils.utils import Utils, DateUtils

logger = logging.getLogger(__name__)


def main():
    """Pyrene main function."""
    logger.info("** Pyrene App - By Atesmaps **")

    # Validate environment
    Utils.validate_environment()

    # Define collection date
    collection_date = DateUtils().collection_date()

    # Run Pyrene process to collect bulletins data
    Pyrene().run(collection_date=collection_date)


main()
