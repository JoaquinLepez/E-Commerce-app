from flask import Blueprint, request
import requests
from ..services import ResponseBuilder, SagaBuilder, CompraService, InventarioService, PagoService, CatalogoService
from ..mapping import ResponseSchema


response_schema = ResponseSchema()

catalogo = CatalogoService()
compra = CompraService()
inventario = InventarioService()
pago = PagoService()

e_commerce = Blueprint('e_commerce', __name__)

@e_commerce.route('/e_commerce', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    response_builder.add_message('Hello, World!').add_status_code(200).add_data({})
    return response_schema.dump(response_builder.build()), 200


@e_commerce.route('/e_commerce/producto/<int:id>', methods=['GET'])
def get_product(id):
    response_builder = ResponseBuilder()
    message = 'No se encontro el producto'
    status_code = 404
    producto = catalogo.obtener_producto(id)
    
    if producto:
        message = 'Producto encontrado'
        status_code = 200

    response_builder.add_message(message).add_status_code(status_code).add_data(producto.json())
    return response_schema.dump(response_builder.build()), status_code

@e_commerce.route('/e_commerce/compra', methods=['POST'])
def create_compra():
    response_builder = ResponseBuilder()
    data = request.json
    response = SagaBuilder()  \
    .action(compra.comprar,compra.borrar_compra) \
    .action(pago.agregar_pago,pago.borrar_pago) \
    .action(inventario.agregar_stock,inventario.borrar_stock) \
    .set_data(data) \
    .build() \
    .execute()
    response_builder.add_data(response['data']).add_status_code(response['status_code']).add_message(response['message'])
    return response_schema.dump(response_builder.build()), response['status_code']

