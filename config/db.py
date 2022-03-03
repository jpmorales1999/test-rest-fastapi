# Permite Interactuar con la BD de Forma Sencilla Mediante Python
from sqlalchemy import create_engine, MetaData

# Conexión a la BD
engine = create_engine('mysql+pymysql://root:@localhost:3306/rest-fastapi')

meta = MetaData()

conn = engine.connect()