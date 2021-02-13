from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import CONTENT_TYPE_LATEST, REGISTRY, generate_latest
try:
    from bme280 import BME280
    from ltr559 import LTR559
except ImportError:
    from mocks import BME280, LTR559

from instruments import Hardware as HardwareInstrument
from models import Sensors as SensorsModel


class InstrumentResponse(PlainTextResponse):
    media_type = CONTENT_TYPE_LATEST


app = FastAPI()
bme280 = BME280()
ltr559 = LTR559()


@app.get('/', response_class=PlainTextResponse)
async def root():
    return 'OK'


@app.get('/json')
async def json():
    return SensorsModel.poll(bme280, ltr559)


@app.get('/metrics', response_class=InstrumentResponse)
async def metrics():
    HardwareInstrument.poll()
    return generate_latest(REGISTRY)
