
from fastapi import FastAPI, Form, Response, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from db import *
from model import UserInDb

from pymongo.errors import PyMongoError
from jinja2 import Environment, select_autoescape, FileSystemLoader





app = FastAPI()
templates = Jinja2Templates(directory='.')




#######################################
##                   / 
######################################
def none_index():
    env = Environment(
        loader=FileSystemLoader('../jinja2 templates'),
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


@app.post('/users/register')
async def users_register(response: Response,
                         username: str = Form(...),
                         phone_number: str = Form(...),
                         password1: str = Form(...),
                         password2: str = Form(...),):

    if not username or not password1 or not password2 or not phone_number:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'massage': 'please fill the form'})
    if password1 != password2:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'massage': 'passwords dont match'})
    form_data = UserInDb(username=username,
                         phone_number=phone_number,
                         hashed_password=password1)
    if check_exist(form_data.username):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'massage': 'user already exist'})
    hashed_pass = password_hash.hash(password1)
    form_data.hs_password = hashed_pass
    try:
        insert_one(dict(form_data))
    except PyMongoError:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={'massage': 'Something went wrong'})

    access_token = create_token(data={'sub': form_data.username})
    response.set_cookie(key='auth_cookie', value=access_token)
    return {'massage': 'register was successful'}

@app.post('/logout')
async def users_logout(request: Request,
                       response: Response):
    response.delete_cookie(key='auth_cookie')
    return RedirectResponse('/')



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
