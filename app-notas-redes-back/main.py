from fastapi import FastAPI
from conection.ConectionDb import ConectionDb
from service.NotaService import NotaService
from entity.Nota import Nota
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://192.168.201.239",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conn = ConectionDb()
conn.initialize()


@app.get("/findAll")
async def findAll():
    return NotaService.findAll()


@app.post("/salvar")
async def salvar(nota: Nota):
    return NotaService.save(nota)


@app.put("/editar")
async def editar(nota: Nota):
    return NotaService.editar(nota)


@app.delete("/deletar/{id}")
async def deletar(id: str):
    return NotaService.deletar(id)
