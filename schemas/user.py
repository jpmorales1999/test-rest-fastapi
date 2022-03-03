# El modulo Typing es la forma de colocar atributos los tipos de datos
from typing import Optional

# El modulo Pydantic nos permite añadir tipos de Datos
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str