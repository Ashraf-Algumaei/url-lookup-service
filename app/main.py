from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK

app = FastAPI()


# Health endpoint
@app.get('/')
async def health(response: Response):
    response.status_code = HTTP_200_OK
    return True
