from typing import List
from azure.cosmos.exceptions import CosmosResourceNotFoundError, CosmosHttpResponseError

from common.cosmos_client_manager import CosmosClientManager


class UrlInfoProvider:
    """
    Provider Class for Cosmos Database
    """

    def __init__(self, db_host, db_master_key):
        self.database = "Urls"
        self.container = "malwareUrls"
        self.cosmos_manager = CosmosClientManager(db_host, db_master_key, self.database,
                                                  self.container)

    def get_url_info(self, url: str) -> dict:
        """
        Sends a GET request to Urls Info Container

        Args:
            url: The specific URL to find the info of

        Returns:
            dict: the response from the database with the details
        """
        if url is None:
            return None
        try:
            response = self.cosmos_manager.get_record(url, url)
            return response
        except (CosmosResourceNotFoundError, CosmosHttpResponseError):
            return None

    def upsert_to_database(self, urls: List[str]) -> dict:
        """
        Sends a POST request to upsert to the container

        Args:
            urls: The specific URL to find the info for

        Returns:
            # TODO
        """
        try:
            self.cosmos_manager.upsert_record(urls)
            return True
        except (CosmosResourceNotFoundError, CosmosHttpResponseError):
            # TODO: logging errors
            return None
