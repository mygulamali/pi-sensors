from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from prometheus_client import CONTENT_TYPE_LATEST, REGISTRY, generate_latest

from instruments import Hardware


class InstrumentResponse(PlainTextResponse):
    media_type = CONTENT_TYPE_LATEST


route = APIRouter()


@route.get('/', response_class=PlainTextResponse)
async def root():
    return 'OK'


@route.get('/hardware', response_class=InstrumentResponse)
async def hardware():
    Hardware.poll()
    return generate_latest(REGISTRY)
