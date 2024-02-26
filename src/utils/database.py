import logging
from os import getenv

logger = logging.getLogger(__name__)


class Database:
    def __init__(self):
        self.conn_string = self._get_conn_string()

    @staticmethod
    def _get_conn_string() -> str:
        """
        Get connection string to connect to PostgreSQL database.

        Returns
        -------
        string
            Connection string with parameters to connect to PostgreSQL database.
        """
        logger.debug("Generating database connection string...")
        return (
            f"host={getenv('DATABASE_HOST')} user={getenv('DATABASE_USER')} "
            f"password={getenv('DATABASE_PASSWORD')} port={getenv('DATABASE_PORT')} "
            f"dbname={getenv('DATABASE_NAME')}"
        )
