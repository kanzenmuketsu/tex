from random import randint

from fastapi import HTTPException, status
from fastapi import FastAPI, Form, Response, Request
from fastapi.responses import  FileResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from jinja2 import Environment, select_autoescape, FileSystemLoader



app = FastAPI()
templates = Jinja2Templates(directory='.')

#######################################
##                   / 
######################################
def none_index():
    env = Environment(
        loader=FileSystemLoader('../jinja2_templates'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('index_jinja.html')
    rendered_page = template.render(
        display='none'
    )
    with open('../templates/index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    return FileResponse('../templates/index.html')

@app.get('/')
async def main():
    return none_index()



@app.get('/users/test')
async def test(request: Request):
    if request.cookies.get('auth_cookie'):
        return {'cookie':request.cookies.get('auth_cookie'),
                'ok': 'ok'}
    return {'cookie':'a',
                'ok': 'ok'}



from redirections import *
if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
