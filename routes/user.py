from fastapi import APIRouter, Response, status

from starlette.status import HTTP_204_NO_CONTENT

from config.db import conn

from models.user import users

from schemas.user import User

from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

user = APIRouter()

@user.get('/users', response_model=list[User], tags=['Users'])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get('/users/{id}', response_model=User, tags=['Users'])
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()

@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Users'])
def delete_user(id: str):
    result = conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.post('/users', response_model=User, tags=['Users'])
def create_user(user: User):
    new_user = { "name": user.name, "email": user.email }
    new_user['password'] = f.encrypt(user.password.encode('utf-8'))
    result = conn.execute(users.insert(new_user))
    # Al crear el usuario busca en la base de datos donde el usuarios en la columna "c" id es igual a el ID que se acaba de registrar y como será una lista nada más se busca el primer dato que será aquel que cumple con la condición
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()

@user.put('/users/{id}', response_model=User, tags=['Users'])
def update_user(id: str, user: User):
    password = f.encrypt(user.password.encode('utf-8'))
    conn.execute(users.update().values(name = user.name, email = user.email, password = password).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()

