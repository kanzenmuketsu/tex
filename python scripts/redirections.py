from app import  app
from fastapi.responses import FileResponse

@app.get('/index.html')
async def main():
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
async def main():
    return FileResponse('../templates/личный-кабинет.html')

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

@app.get('/products/череп.html')
async def main():
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