from PIL import Image,ImageEnhance
import shutil
from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates = Jinja2Templates(directory="templates")
@app.get("/",response_class=HTMLResponse)
def root(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/uploadfile",response_class=FileResponse)
def proc(im=Form()):
    with open("original.jpg","wb") as buffer:
        shutil.copyfileobj(im.file,buffer)
    img=Image.open('original.jpg')
    img.save('reduced.jpg',quality=80)
    return 'reduced.jpg'
@app.post("/processimg",response_class=FileResponse)
def modify(per:int=Form()):
    img=Image.open('original.jpg')
    img.save('reduced.jpg',quality=per)
    return 'reduced.jpg'


