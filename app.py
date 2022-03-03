from turtle import title
from fastapi import FastAPI

from routes.user import user

# Crear Objeto Tipo FastAPI Para Crear El Servidor...
app = FastAPI(
    title="My First FastAPI",
    description="Learn FastAPI",
    version="0.0.1",
    openapi_tags=[{
        "name": "users",
        "description": "Users Routes"
    }]
)

# Configuración de Rutas
app.include_router(user)

