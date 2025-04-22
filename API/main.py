
from flask import Flask, request, Response
from flask_cors import CORS
import random
import json

from API.Coneccion import session
from API.OBJS import Product

app = Flask(__name__)
CORS(app)
@app.route('/')
def ping():
    return Response(json.dumps({"message": "Welcome to 4Ustore"}, ensure_ascii=False), mimetype="application/json")

@app.route('/carusel',methods=['GET'])
def carrusel():
    li_Products = session.query(Product).all()
    result_products = []
    selected_indices = set()  # Para almacenar los índices seleccionados

    while len(result_products) < 5:
        # Generar un índice aleatorio
        numero = random.randint(0, len(li_Products)-1)

        # Si el índice ya ha sido seleccionado, generamos otro
        if numero not in selected_indices:
            selected_indices.add(numero)  # Añadimos el índice al conjunto
            result_products.append(li_Products[numero].to_dict())
        if len(selected_indices) == len(li_Products):
            break

    result = {
        'error': None,
        'data': result_products,
        'status': 'success',
        'message': 'productos recuperados con exito',
        'code': 200
    }
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json")



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)