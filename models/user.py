from curses import meta
from tokenize import String
from sqlalchemy import Table, Column

from sqlalchemy.sql.sqltypes import Integer, String

from config.db import meta, engine

# Meta permite acceder a más propiedades de la Tabla
users = Table('users', meta, Column('id', Integer, primary_key=True), Column('name', String(255)), Column('email', String(255)), Column('password', String(255)))

# Con el Esquema de Tabla, utiliza el Engine para crearla
meta.create_all(engine)