from pydantic import BaseModel


class Nota(BaseModel):
    id: str |None
    nome: str
    descricao: str
    data: str
