import requests
from flask import current_app
from tenacity import retry, stop_after_attempt, wait_random

class PagoService:

    @retry(wait=wait_random(min=3, max=4), stop=stop_after_attempt(3))
    def agregar_pago(self,data):        
        data_pago = data.get('pago')
        response = requests.post(current_app.config['PAGOS_URL'], json=data_pago)
        return response
    
    @retry(wait=wait_random(min=3, max=4), stop=stop_after_attempt(3))
    def borrar_pago(self,id_pago):
        requests.delete(current_app.config['PAGOS_URL'] + f'/{id_pago}')