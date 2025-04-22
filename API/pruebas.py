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

# Leer imagen como binario
with open(r"C:\Users\ramir\Downloads\descarga (6).jpg", "rb") as f:
    imagen_bytes = f.read()

# Crear producto
producto = Product(
    nombre="mackbook pro",
    descripcion="lo  mismo de siempre",
    precio=510050.99,
    segundamano=False,
    stock=500,
    id_vendedor=1,
    image=imagen_bytes
)

# Guardar en base de datos
session.add(producto)
session.commit()
print("Producto insertado con imagen.")
