from sqlalchemy import create_engine, Column, Integer, String, Text, Numeric, Boolean, LargeBinary, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import base64
from decimal import Decimal
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    descripcion = Column(Text)
    precio = Column(Numeric(10, 2))
    segundamano = Column(Boolean)
    stock = Column(Integer, default=0, nullable=False)
    id_vendedor = Column(Integer)
    image = Column(LargeBinary)  # BYTEA en PostgreSQL

    def to_dict(self):
        image_data = base64.b64encode(self.image).decode('utf-8') if self.image else None
        precio = float(self.precio) if isinstance(self.precio, Decimal) else self.precio
        return {
            'id':self.id,
            'nombre':self.nombre,
            'descripcion':self.descripcion,
            'precio':precio,
            'segundamano':self.segundamano,
            'stock':self.stock,
            'id_vendedor':self.id_vendedor,
            'image':image_data
        }

from API.Coneccion import engine  # Usando la conexión ya definida
from API.OBJS import Base

Base.metadata.create_all(engine)  # Crea las tablas si no existen

