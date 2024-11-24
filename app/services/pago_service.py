import requests
from flask import current_app

class PagoService:

    def agregar_pago(self,data):        
        data_pago = data.get('pago')
        response = requests.post(current_app.config['PAGOS_URL'], json=data_pago)
        return response
    
    def borrar_pago(self,data):
        id_pago = data
        requests.delete(current_app.config['PAGOS_URL'] + f'/{id_pago}')