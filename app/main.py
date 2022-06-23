import logging
from fastapi import Depends, FastAPI, HTTPException, Response
from starlette.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from fastapi.security.api_key import APIKeyHeader, APIKey

from constants import Constants
from dto.url_insert_request import UrlInsertRequest
from dto.url_insert_response import UrlInsertResponse
from dto.url_lookup_response import UrlLookupResponse
from providers.url_info_provider import UrlInfoProvider
from services.url_info_service import UrlInfoService

app = FastAPI()
api_key_header = APIKeyHeader(name="Api-Key")


def check_api_key(api_key: str = Depends(api_key_header)):
    if api_key == str(Constants.API_KEY):
        return api_key
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Invalid API Key",
        )


# setup services
url_info_service = UrlInfoService(
    url_info_provider=UrlInfoProvider(db_host=str(Constants.COSMOS_DB_HOST),
                                      db_master_key=str(Constants.COSMOS_DB_MASTER_KEY)))


# Health endpoint
@app.get('/')
async def health(response: Response):
    response.status_code = HTTP_200_OK
    return True


# Get endpoint to check if URL has Malware or Safe
@app.get('/urlinfo/1/{hostname_and_port}/{original_path_and_query_string}', status_code=200, response_model=UrlLookupResponse)
async def url_info(hostname_and_port: str, original_path_and_query_string: str, api_key: APIKey = Depends(check_api_key)):
    # check if the URL is found in the Database
    response = url_info_service.get_url_status(hostname_and_port)
    logging.info(f'Response received for {hostname_and_port}: {response}')
    return response


# Post Endpoint to add websites with Malware
@app.post('/url-insert/1', status_code=200, response_model=UrlInsertResponse)
async def url_insert(request: UrlInsertRequest, api_key: APIKey = Depends(check_api_key)):
    # insert to the database
    response = url_info_service.insert_new_urls(request.urls)
    logging.info(f'Response received for inserting URLs: {response}')
    return response
