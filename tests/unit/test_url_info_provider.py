import os
import sys
import pytest

from collections import namedtuple
from pytest_mock import MockerFixture
from requests_mock import Mocker

testdir = os.path.dirname(__file__)
srcdir = '../../app'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from constants import Constants
from providers.url_info_provider import UrlInfoProvider


@pytest.fixture()
def mock_get_url_info_req(requests_mock: Mocker):

    mock_malware_url = 'mock-malware-url.com'
    url: str = f'{Constants.COSMOS_DB_HOST}/dbs/Urls/colls/malwareUrls/docs/{mock_malware_url}/'

    response_json = {
        'id': url
    }

    requests_mock.get(url, json=response_json)

    return namedtuple('response', response_json.keys())(*response_json.values())


@pytest.fixture
def url_info_provider() -> UrlInfoProvider:
    return UrlInfoProvider(db_host=Constants.COSMOS_DB_HOST,
                                  db_master_key=Constants.COSMOS_DB_MASTER_KEY)


@pytest.fixture
def mock_manager(mocker: MockerFixture):
    mock_manager = mocker.patch('providers.url_info_provider.CosmosClientManager').return_value
    return mock_manager


def test_get_url_info(mock_manager, url_info_provider, mock_get_url_info_req):
    # GIVEN
    malware_url = mock_get_url_info_req.id

    # WHEN
    url_info_provider.get_url_info(url=malware_url)

    # THEN
    mock_manager.get_record.assert_called_with(malware_url, malware_url)
