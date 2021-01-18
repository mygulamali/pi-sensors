from typing import Dict

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import CONTENT_TYPE_LATEST, REGISTRY, generate_latest

from instruments import Hardware as HardwareInstrument
from models import Hardware as HardwareModel


class InstrumentResponse(PlainTextResponse):
    media_type = CONTENT_TYPE_LATEST


app = FastAPI()


@app.get('/', response_class=PlainTextResponse)
async def root():
    return 'OK'


@app.get('/json', response_model=HardwareModel)
async def json():
    return HardwareModel.poll()


@app.get('/metrics', response_class=InstrumentResponse)
async def metrics():
    HardwareInstrument.poll()
    return generate_latest(REGISTRY)
