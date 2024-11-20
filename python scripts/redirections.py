from itertools import product

from starlette.status import HTTP_200_OK

from app import  app
from auth import *
from fastapi import HTTPException, Form, Response
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, select_autoescape, FileSystemLoader
import mails
from db import *
from model import UserInDb
from random import randint

@app.post('/register')
async def users_register(response: Response,
                         username: str = Form(...),
                         email: str = Form(...),
                         password1: str = Form(...),
                         password2: str = Form(...),
                         email_id: str = Form(...),
                         email_code: str = Form(...)):

    if not username or not password1 or not password2 or not email:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'massage': 'please fill the form'})
    if password1 != password2:
        return HTTPException(status_code=status.HTTP_409_CONFLICT)

    if email_id not in mails.CODES:
        id = str(randint(22, 88))
        response.set_cookie(key='id', value=id, expires=120)
        mails.send_email_code(id, email)
        return HTTPException(status_code=status.HTTP_103_EARLY_HINTS, detail=email_id)

    if email_code != mails.CODES[email_id]:
        return HTTPException(status_code=status.HTTP_423_LOCKED)


    form_data = UserInDb(username=username,
                         email=email,
                         hashed_password=password1)
    if check_exist(form_data.username):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'massage': 'user already exist'})

    hashed_pass = password_hash.hash(password1)
    form_data.hashed_password = hashed_pass

    try:
        insert_one(dict(form_data))
    except:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={'massage': 'Something went wrong'})

    access_token = create_token(data={'sub': form_data.username})
    response.set_cookie(key='auth_cookie', value=access_token)
    return HTTPException(status_code=HTTP_200_OK, detail="success")



@app.post('/login')
async def users_login(response: Response,
                      username: str = Form(..., min_length=3),
                      password: str = Form(..., min_length=6),):

    if not username or not password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="please fill the login form")
    if authenticate_form_db(username=username,password=password):
        access_token = create_token(data={'sub': username})
        response.set_cookie(key='auth_cookie', value=access_token, expires=999999)
        return HTTPException(status_code=200)
    return HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT)


@app.post('/logout')
async def users_logout(request: Request,
                       response: Response):
    response.delete_cookie(key='auth_cookie')
    return HTTPException(status_code=HTTP_200_OK)


@app.get('/index.html')
async def main(request: Request):
    if request.cookies.get('auth_cookie'):
        env = Environment(
            loader=FileSystemLoader('../jinja2_templates'),
            autoescape=select_autoescape(['html'])
        )
        template = env.get_template('index_jinja.html')
        rendered_page = template.render(
            display="none"
        )
        with open('../templates/index.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)

        return FileResponse('../templates/личный-кабинет.html')

    return FileResponse('../templates/index.html')



@app.get('/nicepage.css')
async def main():
    return FileResponse('../static/nicepage.css')

@app.get('/index.css')
async def main():
    return FileResponse('../static/index.css')

@app.get('/jquery.js')
async def main():
    return FileResponse('../jquery.js')

@app.get('/custom.js')
async def main():
    return FileResponse('../custom.js')

@app.get('/nicepage.js')
async def main():
    return FileResponse('../nicepage.js')

@app.get('/images/Screenshot2024.png')
async def main():
    return FileResponse('../images/Screenshot2024.png')

@app.get('/images/images.png')
async def main():
    return FileResponse('../images/images.png')

@app.get('/images/sibmed.png')
async def main():
    return FileResponse('../images/sibmed.png')

@app.get('/ssmu.png')
async def main():
    return FileResponse('../images/ssmu.png')

@app.get('/149.png')
async def main():
    return FileResponse('../images/1492.png')

#@app.get('/favicon.ico')
#async def main():
#   return FileResponse(path='images/favicon.png', headers={'Content-Desposition': "attachment; filename=favicon.png"})

#############################
#              лк
#############################
@app.get('/личный-кабинет.html')
async def main(request: Request):
    if request.cookies.get('auth_cookie'):
        env = Environment(
             loader=FileSystemLoader('../jinja2_templates'),
             autoescape=select_autoescape(['html'])
            )
        template = env.get_template('личный-кабинет_jinja.html')
        rendered_page = template.render(
            username=current_user(request.cookies.get('auth_cookie'))
        )
        with open('../templates/личный-кабинет.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)

        return FileResponse('../templates/личный-кабинет.html')

    return FileResponse('../templates/index.html')



@app.get('/личный-кабинет.css')
async def main():
    return FileResponse('../static/личный-кабинет.css')

@app.get('/cxema.png')
async def main():
    return FileResponse('../images/cxema.png')

###########################
#            политика
##########################
@app.get('/политика.html')
async def main():
    return FileResponse('../templates/политика.html')

@app.get('/политика.css')
async def main():
    return FileResponse('../static/политика.css')

#########################
#         Каталог
#########################
@app.get('/Каталог.css')
async def main():
    return FileResponse('../static/Каталог.css')

@app.get('/Каталог.html')
async def main():
    return FileResponse('../templates/Каталог.html')

@app.get('/bones.png')
async def main():
    return FileResponse('../images/bones.png')

@app.get('/calendar.jpeg')
async def main():
    return FileResponse('../images/calendar.jpeg')

####################
#         кости
####################
@app.get('/кости.html')
async def main():

    product1 = list(get_products_from_db(1))
    product2 = list(get_products_from_db(2))

    product1[4] = '' if product1[4] is None else product1[4]
    product2[4] = '' if product2[4] is None else product2[4]
    product1_button = 'Заказать' if  product1[-1] != 0 else 'Нет в наличии'
    product2_button = 'Заказать' if  product2[-1] != 0 else 'Нет в наличии'

    env = Environment(
        loader=FileSystemLoader('../jinja2_templates'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('кости_jinja.html')
    rendered_page = template.render(
        product1_name = product1[1], # name.
        product1_image1 = product1[5], # img1.
        product1_image2 = product1[6], # img2.
        product1_old_price = product1[4], # old price.
        product1_price = product1[3], # price.
        product1_button = product1_button,
        product2_name = product2[1], # name.
        product2_image1 = product2[5], # img1.
        product2_image2 = product2[6], # img2.
        product2_old_price = product2[4], # old price.
        product2_price = product2[3], # price.
        product2_button = product2_button
    )
    with open('../templates/кости.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    return FileResponse('../templates/кости.html')

@app.get('/кости.css')
async def main():
    return FileResponse('../static/кости.css')

@app.get('/images/images1.jpg')
async def main():
    return FileResponse('../images/images1.jpg')

@app.get('/images/images1.png')
async def main():
    return FileResponse('../images/images1.png')

@app.get('/images/scull1.jpg')
async def main():
    return FileResponse('../images/scull1.jpg')

@app.get('/images/girl.png')
async def main():
    return FileResponse('../images/girl.png')

@app.get('/products/products.json')
async def main():
    return FileResponse('../prod.json')


@app.get('/products/{page}.html', response_class=HTMLResponse)
async def main(pagename: str):
    print(pagename)
    product = list(get_products_from_db(1))
    product[4] = '' if product[4] is None else product[4]
    product_button = 'Заказать' if product[-1] != 0 else 'Нет в наличии'

    env = Environment(
        loader=FileSystemLoader('../jinja2_templates'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('череп_jinja.html')
    rendered_page = template.render(
        product_name=product[1],  # name.
        product_info=product[2],  # name.
        product_image1=product[5],  # img1.
        product_image2=product[6],  # img2.
        product_image3=product[7],  # img3.
        product_old_price=product[4],  # old price.
        product_price=product[3],  # price.
        product_button=product_button
    )
    with open('../templates/череп.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    return FileResponse('../templates/череп.html')

@app.get('/Product-Details-Template.css')
async def main():
    return FileResponse('../static/Product-Details-Template.css')

@app.get('/images/Skull.jpg')
async def main():
    return FileResponse('../images/Skull.jpg')

@app.get('/images/Avtor-Mathew-Schwartz-Istochnik-unsplash-1-scaled-Photoroom1.png')
async def main():
    return FileResponse('../images/bones.png')

@app.get('/images/photo-1641386337567-c824f91bea87.jpeg')
async def main():
    return FileResponse('../images/calendar.jpeg')

@app.get('/products/тестовый-слепок.html')
async def main():
    return FileResponse('../templates/тестовый-слепок.html')

@app.get('/images/testbone.png')
async def main():
    return FileResponse('../images/testbone.png')

########################
#      о нас
#######################
@app.get('/О-нас.html')
async def main():
    return FileResponse('../templates/О-нас.html')

@app.get('/О-нас.css')
async def main():
    return FileResponse('../static/О-нас.css')

@app.get('/images/vk.png')
async def main():
    return FileResponse('../images/vk.png')

@app.get('/images/tg.png')
async def main():
    return FileResponse('../images/tg.png')

@app.get('/images/circle.png')
async def main():
    return FileResponse('../images/circle.png')
#
@app.get('/images/misha.jpg')
async def main():
    return FileResponse('../images/misha.jpg')

@app.get('/images/mishaDoc.jpg')
async def main():
    return FileResponse('../images/mishaDoc.jpg')

@app.get('/images/prisonerBonny.jpg')
async def main():
    return FileResponse('../images/prisonerBonny.jpg')

@app.get('/images/corpus.jpg')
async def main():
    return FileResponse('../images/corpus1.jpg')

@app.get('/images/pavshiy.jpg')
async def main():
    return FileResponse('../images/pavshiy.jpg')
#################k
#  блог
##################
@app.get('/блог.html')
async def main():
    return FileResponse('../templates/блог.html')

@app.get('/блог.css')
async def main():
    return FileResponse('../static/блог.css')

@app.get('/images/background.png')
async def main():
    return FileResponse('../images/background.png')

@app.get('/images/berserk.jpg')
async def main():
    return FileResponse('../images/berserk.jpg')

@app.get('/images/prince.jpg')
async def main():
    return FileResponse('../images/prince.jpg')

@app.get('/images/images.jpg')
async def main():
    return FileResponse('../images/images.jpg')

@app.get('/images/girl2.png')
async def main():
    return FileResponse('../images/girl2.png')

@app.get('/files/video.mp4')
async def main():
    return FileResponse('../files/video.mp4')

@app.get('/images/tgscreen.png')
async def main():
    return FileResponse('../images/tgscreen.png')

@app.get('/images/fan1.png')
async def main():
    return FileResponse('../images/fan1.png')

@app.get('/images/fan2.png')
async def main():
    return FileResponse('../images/fan2.png')

@app.get('/images/fan3.png')
async def main():
    return FileResponse('../images/fan3.png')

@app.get('/images/comment.png')
async def main():
    return FileResponse('../images/comment.png')
###################################
#      корзиеа
##################################
@app.get('/корзина.html')
async def main():
    return FileResponse('../templates/корзина.html')

@app.get('/корзина.css')
async def main():
    return FileResponse('../static/корзина.css')