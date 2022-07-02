import os
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


@app.post("/uploadfile")
def proc(im=Form()):
    with open("original.jpg","wb") as buffer:
        shutil.copyfileobj(im.file,buffer)
    img=Image.open('original.jpg')
    img.save('/home/pranoydhar/Downloads/techsurf/submission/static/reduced.jpg',quality=81)
    xk=Image.open('/home/pranoydhar/Downloads/techsurf/submission/static/reduced.jpg')
    xk.close()
    return {"foo":'True'}
@app.post("/processimg")
def modify(qua:int=Form()):
    img=Image.open('original.jpg')
    img.save('/home/pranoydhar/Downloads/techsurf/submission/static/reduced.jpg',quality=qua)
    xk=Image.open('/home/pranoydhar/Downloads/techsurf/submission/static/reduced.jpg')
    xk.close()
    return {"foo":'True'}
@app.get("/downloadfile")
def download_file():
    filepath='/home/pranoydhar/Downloads/techsurf/submission/static/reduced.jpg'
    return FileResponse(path=filepath,media_type='application/octet-stream',filename=filepath)
