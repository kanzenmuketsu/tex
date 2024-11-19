
from auth import current_user, check_exist

from fastapi import HTTPException, status
from fastapi import FastAPI, Form, Response, Request
from fastapi.responses import  FileResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import uvicorn



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
async def main(request: Request):
    return FileResponse('../templates/О-нас.html')
    #if request.cookies.get('auth_cookie'):
        #if check_exist(current_user(request.cookies.get('auth_cookie'))):
            #return FileResponse('../templates/личный-кабинет.html')
    #return none_index()




from redirections import *
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)