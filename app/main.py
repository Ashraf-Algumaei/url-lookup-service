from fastapi import Depends, FastAPI, HTTPException, Response
from starlette.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from fastapi.security.api_key import APIKeyHeader, APIKey

from constants import Constants

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


# Health endpoint
@app.get('/')
async def health(response: Response):
    response.status_code = HTTP_200_OK
    return True


# Get endpoint to check if URL has Malware or Safe
@app.get('/urlinfo/1/{hostname_and_port}/{original_path_and_query_string}', status_code=200)
async def url_info(hostname_and_port: str, original_path_and_query_string: str, api_key: APIKey = Depends(check_api_key)):
    return True