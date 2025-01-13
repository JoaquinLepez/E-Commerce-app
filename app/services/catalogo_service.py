import requests
from tenacity import retry, stop_after_attempt, wait_random
from flask import current_app
from app.mapping import ProductoSchema

schema = ProductoSchema()

class CatalogoService:
    
    @retry(wait=wait_random(min=3, max=4), stop=stop_after_attempt(3))
    def obtener_producto(self, id_producto):
        r = requests.get(current_app.config['CATALOGO_URL'] + f'{id_producto}')
        if r.status_code != 200:
            return None
        producto = schema.load(r.json())
        return producto
