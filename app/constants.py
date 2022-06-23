from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")


class Constants:
    API_KEY = config('API_KEY', cast=Secret, default='test')
    COSMOS_DB_HOST = config('COSMOS_DB_HOST', cast=Secret, default="https://url-lookup-east-cosmos-db.documents.azure.com:443/")
    COSMOS_DB_MASTER_KEY = config('COSMOS_DB_MASTER_KEY', cast=Secret, default="")
    SAFE_URL_MESSAGE = "SAFE"
    MALWARE_URL_MESSAGE = "MALWARE"
    APP_INSIGHTS_CONNECTION_STRING = config('APP_INSIGHTS_CONNECTION_STRING', cast=Secret, default='')
