from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.database import engine, SessionLocal
import db.models as models
import schemas 
import services

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/styles", StaticFiles(directory="./templates/styles"), name="styles")
app.mount("/assets", StaticFiles(directory="./templates/assets"), name="assets")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def home(req: Request):
    return templates.TemplateResponse("index.html", {"request": req})

@app.get("/juiz", response_class=HTMLResponse)
async def juiz(req: Request):
    return templates.TemplateResponse("juiz.html", {"request": req})

@app.post("/addjuiz", response_class=HTMLResponse)
async def add_juiz(req: Request, full_name: str = Form(...), db: Session = Depends(get_db)):
    juiz_create = schemas.JuizCreate(full_name=full_name)
    services.create_juiz(db=db, juiz=juiz_create)
    return templates.TemplateResponse("juiz.html", {"request": req, "message": "Juiz adicionado com sucesso!"})

@app.get("/sentenciado", response_class=HTMLResponse)
async def sentenciado(req: Request):
    return templates.TemplateResponse("sentenciado.html", {"request": req})

@app.post("/addsentenciado", response_class=HTMLResponse)
async def add_sentenciado(
    req: Request, 
    name: str = Form(...),
    felony: str = Form(...),
    sentence: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        sentence_enum = schemas.SentencasEnum(sentence)
    except ValueError:
        raise HTTPException(status_code=400, detail="Sentença inválida!")

    sentenciado_create = schemas.SentenciadoCreate(
        name=name,
        felony=felony,
        sentence=sentence_enum
    )
    services.create_sentenciado(db=db, sentenciado=sentenciado_create)
    return templates.TemplateResponse("sentenciado.html", {"request": req, "message": "Sentenciado adicionado com sucesso!"})

@app.get("/sentencas", response_class=HTMLResponse)
async def sentenciados(req: Request, db: Session = Depends(get_db)):
    sentenciados = services.get_sentenciados(db=db)
    return templates.TemplateResponse("sentenciados.html", {"request": req, "sentenciados": sentenciados})

@app.get("/edit/{sentenciado_id}", response_class=HTMLResponse)
async def edit_sentenciado(req: Request, sentenciado_id: int, db: Session = Depends(get_db)):
    sentenciado = services.get_sentenciado(db=db, sentenciado_id=sentenciado_id)
    if sentenciado is None:
        raise HTTPException(status_code=404, detail="Sentenciado não encontrado")
    return templates.TemplateResponse("edit.html", {"request": req, "sentenciado": sentenciado})


@app.post("/update/{sentenciado_id}", response_class=HTMLResponse)
async def update_sentenciado(
    req: Request, 
    sentenciado_id: int,
    name: str = Form(...),
    felony: str = Form(...),
    sentence: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        sentence_enum = schemas.SentencasEnum(sentence)
    except:
        raise HTTPException(status_code=400, detail="Sentença inválida!")

    sentenciado_update = schemas.SentenciadoCreate(
        name=name,
        felony=felony,
        sentence=sentence_enum
    )

    updated_sentenciado = services.update_sentenciado(db=db, sentenciado_id=sentenciado_id, sentenciado_update=sentenciado_update)
    if updated_sentenciado is None:
        raise HTTPException(status_code=404, detail="Sentenciado não encontrado!")

    return RedirectResponse(url="/sentencas", status_code=303)

@app.get("/delete/{sentenciado_id}", response_class=HTMLResponse)
async def delete_sentenciado(
    req: Request,
    sentenciado_id: int,
    db: Session = Depends(get_db)
):
    deleted_sentenciado = services.delete_sentenciado(db=db, sentenciado_id=sentenciado_id)
    if deleted_sentenciado is None:
        raise HTTPException(status_code=404, detail="Sentenciado não encontrado")

    return RedirectResponse(url="/sentencas", status_code=303)