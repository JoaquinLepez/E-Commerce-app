import requests
from flask import current_app
from tenacity import retry, stop_after_attempt, wait_random

class CompraService:

    @retry(wait=wait_random(min=3, max=4), stop=stop_after_attempt(3))
    def comprar(self,data):
        data_compra = data.get('compra')
        response = requests.post(current_app.config['COMPRAS_URL'], json=data_compra)
        return response
    
    @retry(wait=wait_random(min=3, max=4), stop=stop_after_attempt(3))
    def borrar_compra(self,id_compra):
        requests.delete(current_app.config['COMPRAS_URL'] + f'/{id_compra}')
