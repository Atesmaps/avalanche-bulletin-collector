import logging
from os import getenv
from datetime import datetime

from src.utils import constants as ct

logger = logging.getLogger(__name__)


class Utils:
    @staticmethod
    def validate_environment() -> bool:
        """
        Validate if the required environment variables are present.

        Returns
        -------
        bool
            True if all required variables are present.
        """
        logger.debug("Validating environment...")
        missing_env = []

        for env_var in ct.REQUIRED_ENV_VARIABLES:
            if not getenv(env_var):
                missing_env.append(env_var)

        if missing_env:
            logger.critical("Environment is not valid.")
            raise ValueError(
                f"The following environment variables are required: {','.join(missing_env)}"
            )

        logger.debug("Environment is valid.")
        return True


class DateUtils:
    def __init__(self):
        pass

    @staticmethod
    def validate_format(date_str: str) -> datetime | bool:
        """
        Check if provided string is a valid date in format 'YYYY-MM-DD'.

        Parameters
        ----------
        date_str: str
            The string with date to validate format 'YYYY-MM-DD'.

        Returns
        -------
        datetime | bool
            If date is valid return the date object. Return False instead.
        """
        try:
            logger.debug(
                f"Checking if the string {date_str!r} is in format 'YYYY-MM-DD' and is valid..."
            )
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            logger.error(f"The string {date_str!r} is not a valid date.")
            return False

    def collection_date(self) -> datetime:
        """
        Defines the date from which the avalanche
        bulletin data will be collected.

        Returns
        -------
        datetime
            The collection date to read the avalanche bulletins.
        """
        logger.debug("Defining the collection date...")

        # Use custom date if it's set
        custom_date = getenv("CUSTOM_DATE")
        if custom_date:
            date_obj = self.validate_format(date_str=custom_date)
            if date_obj:
                return date_obj
            else:
                raise ValueError(
                    f"The selected custom date {custom_date!r} is not valid."
                )

        # Use today instead
        return datetime.now().strftime("%Y-%m-%d")
