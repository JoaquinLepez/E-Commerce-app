import requests
from flask import current_app
from tenacity import retry, stop_after_attempt, wait_random

class InventarioService:

    @retry(wait=wait_random(min=3, max=4), stop=stop_after_attempt(3))
    def agregar_stock(self,data):
        data_stock = data.get('stock')
        response = requests.post(current_app.config['INVENTARIO_URL'], json=data_stock)
        return response

    @retry(wait=wait_random(min=3, max=4), stop=stop_after_attempt(3))
    def borrar_stock(self,id_stock):
        requests.delete(current_app.config['INVENTARIO_URL'] + f'/{id_stock}')

