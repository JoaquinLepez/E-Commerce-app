from flask import Blueprint, request
import requests
from .services import OrquestadorSaga, ResponseBuilder
from .mapping import ResponseSchema

response_schema = ResponseSchema()
saga = OrquestadorSaga()

e_commerce = Blueprint('e_commerce', __name__)

@e_commerce.route('/e_commerce', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    response_builder.add_message('Hello, World!').add_status_code(200).add_data({})
    return response_schema.dump(response_builder.build()), 200

@e_commerce.route('/e_commerce/producto/<int:producto_id>', methods=['GET'])
def get_product(producto_id):
    response_builder = ResponseBuilder()
    r = requests.get(f'http://127.0.0.1:3001/api/v1/productos/{producto_id}')
    if r.status_code == 200:
        data = r.json().get('data')
        response_builder.add_data(data).add_status_code(200).add_message('Producto found')
        return response_schema.dump(response_builder.build()), 200
    else:
        data = r.json().get('data')
        response_builder.add_data(data).add_status_code(404).add_message('Producto not found')
        return response_schema.dump(response_builder.build()), 404

@e_commerce.route('/e_commerce/compra', methods=['POST'])
def create_compra():
    response_builder = ResponseBuilder()
    data_compra = request.json
    data, message, status_code = saga.add_compra(data_compra)
    return response_schema.dump(response_builder.add_data(data).add_message(message).add_status_code(status_code).build()), status_code


