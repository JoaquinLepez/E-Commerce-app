import requests
from flask import current_app

class CompraService:

    def comprar(self,data):
        data_compra = data.get('compra')
        response = requests.post(current_app.config['COMPRAS_URL'], json=data_compra)
        return response
    
    def borrar_compra(self,data):
        id_compra = data
        requests.delete(current_app.config['COMPRAS_URL'] + f'/{id_compra}')
