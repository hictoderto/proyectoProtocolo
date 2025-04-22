from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from API.OBJS import Product

# Cargar variables desde el archivo .env
load_dotenv()

# Obtenerlas con os.getenv
usuario = os.getenv("DB_USER")
contraseña = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
puerto = os.getenv("DB_PORT")
base_datos = os.getenv("DB_NAME")

# Crear URL de conexión
url = f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}"
engine = create_engine(url)

Session = sessionmaker(bind=engine)
session = Session()


