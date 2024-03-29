import datetime
import logging
from os import getenv

from src.utils import constants as ct

logger = logging.getLogger(__name__)


class Pyrene:
    def __init__(self):
        self.bulletins = self._set_bulletins()

    @staticmethod
    def _set_bulletins() -> list:
        """
        Returns
        -------
        list
            The List with selected bulletins. By default, use all.
        """
        custom_bulletin = getenv("CUSTOM_BULLETIN")
        if custom_bulletin:
            logger.debug(f"Custom bulletin {custom_bulletin!r} selected.")
            return [custom_bulletin]
        else:
            return ct.SUPPORTED_BULLETINS

    @staticmethod
    def collect_bulletin(bulletin: str, collection_date: datetime):
        """
        Collects the avalanche bulletin data for provided region and date.

        Parameters
        ----------
        bulletin: str
            The id of the bulletin from which the data will be collected.
        collection_date: datetime
            The date used for collect data from avalanche bulletins.
        """
        logger.info(f"Collecting data for bulletin: {bulletin!r}")
        if bulletin == "aran":
            from bulletins import aran

            aran.AranBulletin(collection_date=collection_date).run()

    def run(self, collection_date: datetime) -> None:
        """
        Run the avalanche bulletin collector process for selected date.

        Parameters
        ----------
        collection_date: datetime
            The date used for collect data from avalanche bulletins.

        Returns
        -------
            None
        """
        logger.info("Running avalanche bulletin collector process...")
        logger.info(f"Selected collection date: {collection_date}")
        for bulletin in self.bulletins:
            self.collect_bulletin(
                bulletin=bulletin,
                collection_date=collection_date,
            )
