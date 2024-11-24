from flask import Blueprint, current_app, request
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
    r = requests.get(current_app.config['CATALOGO_URL'] + f'{id}')

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

