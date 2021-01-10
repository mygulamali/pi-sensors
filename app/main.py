from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from models import Hardware


app = FastAPI()


@app.get('/', response_class=PlainTextResponse)
async def root():
    return 'OK'


@app.get('/hardware')
async def hardware():
    return Hardware.poll()

