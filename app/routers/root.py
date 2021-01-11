from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from models import Hardware


route = APIRouter()


@route.get('/', response_class=PlainTextResponse)
async def root():
    return 'OK'


@route.get('/hardware')
async def hardware():
    return Hardware.poll()
