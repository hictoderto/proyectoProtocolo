from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Cargar las variables de entorno
load_dotenv()

# Obtener las variables desde el archivo .env
usuario = os.getenv("DB_USER")
contraseña = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
puerto = os.getenv("DB_PORT")
base_datos = os.getenv("DB_NAME")

# Verificar que las variables de entorno se están cargando correctamente
print("DB_USER:", usuario)
print("DB_PASSWORD:", contraseña)
print("DB_HOST:", host)
print("DB_PORT:", puerto)
print("DB_NAME:", base_datos)

# Crear la URL de conexión
url = f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}"
# Crear el engine de SQLAlchemy
engine = create_engine(url)

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

