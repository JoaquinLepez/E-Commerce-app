import requests
from flask import current_app

class InventarioService:

    def agregar_stock(self,data):
        data_stock = data.get('stock')
        response = requests.post(current_app.config['INVENTARIO_URL'], json=data_stock)
        return response
    
    def borrar_stock(self,data):
        id_stock = data
        requests.delete(current_app.config['INVENTARIO_URL'] + f'/{id_stock}')

