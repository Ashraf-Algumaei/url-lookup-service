from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")


class Constants:
    API_KEY = config('API_KEY', cast=Secret, default='test')