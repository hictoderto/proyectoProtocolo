from flask import Flask, request, jsonify
from flask_cors import CORS
from API.Coneccion import session
from API.OBJS import Product
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)
CORS(app)  # Para habilitar CORS, si lo necesitas para el front-end

# Ruta de inicio
@app.route('/')
def ping():
    return jsonify({"message": "Bienvenido a 4Ustore API!"})

# Ruta para obtener los productos (por ejemplo, para el carrusel)
@app.route('/productos', methods=['GET'])
def obtener_productos():
    try:
        productos = session.query(Product).all()
        productos_lista = [producto.to_dict() for producto in productos]
        return jsonify({"data": productos_lista, "message": "Productos obtenidos con éxito!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ruta para subir producto
@app.route('/upload-product', methods=['POST'])
def upload_product():
    try:
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = float(request.form['precio'])
        stock = int(request.form['stock'])
        segundamano = request.form['segundamano'] == 'true'  # Convertirlo a booleano

        # Leer la imagen del producto
        image_file = request.files['image']
        image_data = image_file.read()  # Leer la imagen como bytes

        # Crear un nuevo objeto Producto
        nuevo_producto = Product(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            segundamano=segundamano,
            image=image_data,
            id_vendedor=1  # Aquí puedes modificar el id del vendedor según sea necesario
        )

        # Guardar el producto en la base de datos
        session.add(nuevo_producto)
        session.commit()

        return jsonify({"message": "Producto subido exitosamente!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
