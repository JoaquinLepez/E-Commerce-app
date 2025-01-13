from flask import Blueprint, request
from app.services import ResponseBuilder, EcommerceService
from ..mapping import ResponseSchema

response_schema = ResponseSchema()
ecommerce_service = EcommerceService()

e_commerce = Blueprint('e_commerce', __name__)

@e_commerce.route('/e_commerce', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    response_builder.add_message('Hello, World!').add_status_code(200)
    return response_schema.dump(response_builder.build()), 200


@e_commerce.route('/e_commerce/producto/<int:id>', methods=['GET'])
def consultar_producto(id):
    message = 'No se encontro el producto'
    status_code = 404
    response_builder = ResponseBuilder()
    producto = ecommerce_service.consultar_producto(id)

    if producto:
        message = 'Producto encontrado'
        status_code = 200
    
    response_builder.add_message(message).add_status_code(status_code).add_data(producto)
    return response_schema.dump(response_builder.build()), status_code

@e_commerce.route('/e_commerce/compra', methods=['POST'])
def comprar_producto():
    response_builder = ResponseBuilder()
    compra_data = request.get_json()
    compra = ecommerce_service.comprar_producto(compra_data)

    response_builder.add_data(compra['data']).add_status_code(compra['status_code']).add_message(compra['message'])
    return response_schema.dump(response_builder.build()), compra['status_code']
