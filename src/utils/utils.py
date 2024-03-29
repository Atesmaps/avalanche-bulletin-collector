import logging
from os import getenv
from datetime import datetime
import requests

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

    @staticmethod
    def get_request(url: str, payload: dict = None) -> dict:
        """
        Do an HTTP request and return response.

        Parameters
        ----------
        url: str
            The URL that you want to get data.
        payload: dict, optional
            Object with payload to add to send toh GET request.

        Returns
        -------
        dict
            Object with response loaded from JSON.
        """
        response = {}
        try:
            logger.debug(f"Running GET request from: {url!r}")
            response = requests.get(
                url=url,
                data=payload,
            )
            response.raise_for_status()
            response = response.json()
            return response
        except requests.exceptions.RequestException as exc:
            logger.error(f"An error occurred: {exc}")
        finally:
            return response

    @staticmethod
    def safe_get(data: dict, keys: list, default=None) -> dict | None:
        """
        Attempts to get a value from a nested dictionary or list using a list of keys/indices.
        Returns `default` if any key/index does not exist.

        Parameters
        ----------
        data : dict
            The dictionary or list from which to get the values.
        keys : list
            A list of keys/indices to access the desired value.
        default : object, optional
            The default value to return if the full path is not found. Default is None.

        Returns
        -------
        dict
            The value obtained from the dictionary/list or the default value.
        """
        for key in keys:
            try:
                if isinstance(data, dict) and key in data:
                    data = data[key]
                elif (
                    isinstance(data, list)
                    and isinstance(key, int)
                    and -len(data) <= key < len(data)
                ):
                    data = data[key]
                else:
                    return default
            except (TypeError, KeyError, IndexError):
                return default
        return data


class DateUtils:
    def __init__(self):
        pass

    @staticmethod
    def validate_format(date_str: str) -> datetime.date:
        """
        Check if provided string is a valid date in format 'YYYY-MM-DD'.

        Parameters
        ----------
        date_str: str
            The string with date to validate format 'YYYY-MM-DD'.

        Returns
        -------
        datetime
            If date is valid return the date object. Return False instead.
        """
        try:
            logger.debug(
                f"Checking if the string {date_str!r} is in format 'YYYY-MM-DD' and is valid..."
            )
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            logger.error(f"The string {date_str!r} is not a valid date.")
            return None

    def collection_date(self) -> datetime.date:
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
        return datetime.now().date()
