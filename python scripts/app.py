from typing import Annotated

from fastapi import FastAPI, Form, Response, Depends, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from db import *
from model import UserInDb
from auth import password_hash, create_token, current_user, authenticate_form_db

from starlette import status

from pymongo.errors import PyMongoError




app = FastAPI()
templates = Jinja2Templates(directory='.')





#######################################
##                   / 
######################################

@app.get('/')
async def main():
    login = False
    if login:
        return FileResponse('../templates/личный-кабинет.html')
    else:
        return FileResponse('../templates/index.html')


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

@app.post('/users/logout')
async def users_logout(request: Request,
                       response: Response):
    response.delete_cookie(key='auth_cookie')
    return {'detail': 'successfuly logout'}

@app.post('/login')
async def users_login(response: Response,
                      username: str = Form(..., min_length=3),
                      password: str = Form(..., min_length=6),):

    if not username or not password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="please fill the login form")
    if authenticate_form_db(username=username,password=password):
        access_token = create_token(data={'sub': username})
        response.set_cookie(key='auth_cookie', value=access_token)
        return HTTPException(status_code=200)
    return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='something went wrong')

@app.post('/t')
async def test():
        return {'ok': 'ok'}

@app.get('/users/test')
async def test(request: Request):
    if request.cookies.get('auth_cookie'):
        return {'cookie':request.cookies.get('auth_cookie'),
                'ok': 'ok'}
    return




from redirections import *

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
