from typing import List
from constants import Constants
from dto.url_insert_response import UrlInsertResponse
from dto.url_lookup_response import UrlLookupResponse
from providers.url_info_provider import UrlInfoProvider


class UrlInfoService:
    """
    Service Class for URL Info Service
    """

    def __init__(self, url_info_provider: UrlInfoProvider):
        self.url_info_provider: UrlInfoProvider = url_info_provider
        self.urlLookupServiceResponse = UrlLookupResponse()
        self.urlInsertServiceResponse = UrlInsertResponse()

    def get_url_status(self, url: str) -> UrlLookupResponse:
        """
        Gets the URL status from the URL Info Provider

        Args:
            url: the URL requested to check if it is in the malware blacklist

        Returns:
            UrlLookupServiceResponse with status of the URL
        """
        url_info_response = self.url_info_provider.get_url_info(url)

        if url_info_response is None:
            self.urlLookupServiceResponse.hostName = url
            self.urlLookupServiceResponse.status = Constants.SAFE_URL_MESSAGE
        else:
            self.urlLookupServiceResponse.hostName = url_info_response['id']
            self.urlLookupServiceResponse.status = Constants.MALWARE_URL_MESSAGE

        return self.urlLookupServiceResponse

    def insert_new_urls(self, urls: List[str]) -> UrlInsertResponse:
        """
        Inserts New URLs using the URL Info Provider

        Args:
            urls: List of URLs to insert to the Database
        Returns:
            UrlInsertResponse instance with values
        """
        url_info_response = self.url_info_provider.upsert_to_database(urls)
        if url_info_response is None:
            self.urlInsertServiceResponse.status = "Failed"

        return self.urlInsertServiceResponse
