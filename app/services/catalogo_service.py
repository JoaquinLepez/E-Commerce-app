import requests
from tenacity import retry, stop_after_attempt, wait_random
from flask import current_app
from app.mapping import ProductoSchema

schema = ProductoSchema()

class CatalogoService:

    @retry(wait=wait_random(min=1, max=2), stop=stop_after_attempt(3))
    def obtener_producto(self, id_producto):
        r = requests.get(current_app.config['CATALOGO_URL'] + f'{id_producto}')
        if r.status_code != 200:
            return None
        producto = schema.load(r.json())
        return producto



    # def obtener_producto(self, id):
    #     producto = cache.get(f"producto_{id}")
    #     if producto is None:
    #          r = requests.get(current_app.config['CATALOGO_URL'] + f'{id}')
    #          if r.status_code == 200:
    #               producto = schema.load(r.json())
    #               cache.set(f"producto_{id}", producto, timeout=100)
    #          else:
    #               raise BaseException("Error en el servicio 1")
    #     return producto
        # producto = cache.get('producto_' + str(id))
        # if producto is None:
        #     r = requests.get(current_app.config['CATALOGO_URL'] + f'{id}')
        #     producto = schema.load(r.json())
        #     cache.set('producto_' + str(id), producto, timeout=100)
        # return producto
  
    
    



#  @retry(wait=wait_random(min=1, max=2), stop=stop_after_attempt(3))
#     def obtener_producto(self, id: int) -> Producto:
#         result = None
#         r = requests.get(f'{self.URL}catalogo/productos/{id}')
#         if r.status_code == 200:
#             result = producto_schema.load(r.json())
#         else:
#             raise BaseException("Error en el servicio 1")
#         return result