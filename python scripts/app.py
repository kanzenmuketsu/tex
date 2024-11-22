from fastapi import FastAPI, Request
#from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.responses import FileResponse



app = FastAPI()
#templates = Jinja2Templates(directory='.')

@app.get('/')
async def main(request: Request):
    return FileResponse('../templates/О-нас.html')

from redirections import *


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)