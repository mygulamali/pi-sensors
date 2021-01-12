from fastapi import FastAPI

from routers import prometheus, root


app = FastAPI()

app.include_router(root)
app.include_router(prometheus, prefix='/prometheus')
