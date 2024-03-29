#################################################
#
#   Pyrene - Avalanche Bulletin Collector - Aran
#
#   Ref: https://lauegi.report
#
#   February 2024 - Atesmaps
#
#################################################
import logging
import datetime
from datetime import timedelta

from pyrene import bpa_urls as bu
from utils.utils import Utils

logger = logging.getLogger(__name__)


class AranBulletin:
    def __init__(self, collection_date: datetime.date):
        self.collection_date = collection_date

    @staticmethod
    def _get_bpa_url(collection_date: datetime.date) -> str:
        """
        Return URL bulletin formatted with date.

        Parameters
        ----------
        collection_date: datetime
            The date used for collect data from avalanche bulletin.

        Returns
        -------
        str
            Formatted URL with selected date.
        """
        return bu.BPA_URL_ARAN_FORMATTABLE.format(
            date=collection_date.strftime("%Y-%m-%d")
        )

    @staticmethod
    def _get_bpa_data(url: str) -> dict:
        """
        Return bulletin data for provided URL.

        Parameters
        ----------
        url: str
            The URL to fetch avalanche bulletin data.

        Returns
        -------
        dict
            Object with full response from avalanche bulletin.
        """
        return Utils().get_request(url=url)

    @staticmethod
    def _curate_bulletin_data(bulletin_data: dict) -> dict:
        """
        Process full data from avalanche bulletin and return curated object.

        Parameters
        ----------
        bulletin_data: dict
            Object with avalanche bulletin data.

        Returns
        -------
        dict:
            Curated object with custom data from bulletin.
        """
        from utils.utils import Utils

        curated_data = {}
        try:
            bulletin_data = bulletin_data["bulletins"][0]
            curated_data = {
                "publication_time": Utils.safe_get(bulletin_data, ["publicationTime"]),
                "avalanche_activity_highlights": Utils.safe_get(
                    bulletin_data, ["avalancheActivity", "highlights"]
                ),
                "avalanche_activity_comment": Utils.safe_get(
                    bulletin_data, ["avalancheActivity", "comment"]
                ),
                "snowpack_structure_comment": Utils.safe_get(
                    bulletin_data, ["snowpackStructure", "comment"]
                ),
                "tendency_highlights": Utils.safe_get(
                    bulletin_data, ["tendency", 0, "highlights"]
                ),
                "tendency_type": Utils.safe_get(
                    bulletin_data, ["tendency", 0, "tendencyType"]
                ),
                "avalanche_problem_type_1": Utils.safe_get(
                    bulletin_data, ["avalancheProblems", 0, "problemType"]
                ),
                "avalanche_problem_elevation_1": Utils.safe_get(
                    bulletin_data,
                    ["avalancheProblems", 0, "elevation", 0, "lowerBound"],
                ),
                "avalanche_problem_snowpack_stability_1": Utils.safe_get(
                    bulletin_data, ["avalancheProblems", 0, "snowpackStability"]
                ),
                "avalanche_problem_frequency_1": Utils.safe_get(
                    bulletin_data, ["avalancheProblems", 0, "frequency"]
                ),
                "avalanche_problem_avalanche_size_1": Utils.safe_get(
                    bulletin_data, ["avalancheProblems", 0, "avalancheSize"]
                ),
                "avalanche_problem_aspects_1": Utils.safe_get(
                    bulletin_data, ["avalancheProblems", 0, "aspects"]
                ),
            }
        except KeyError as exc:
            logger.error("Couldn't curate bulletin data.")
            logger.error(f"ERROR: {exc}")

        return curated_data

    def run(self) -> None:
        """
        Run process that updates data from Aran zone.
        On the first attempt, it will try to obtain avalanche bulletin
        data for collection date + 1, but if no data is available original
        collection date will be used.

        Returns
        -------
        None
        """
        # Selected date (+1 days) attempt
        tomorrow = self.collection_date + timedelta(days=1)
        logger.debug(f"Trying to fetch data from selected date + 1: {tomorrow}")
        bpa_url = self._get_bpa_url(
            collection_date=tomorrow,
        )
        data = self._get_bpa_data(url=bpa_url)
        if not data:
            # Selected data attempt
            logger.debug("No data found for previous date.")
            logger.debug(f"Using selected date: {self.collection_date}")
            data = self._get_bpa_data(url=self._get_bpa_url(self.collection_date))

        curated_data = self._curate_bulletin_data(bulletin_data=data)
        print(curated_data)
