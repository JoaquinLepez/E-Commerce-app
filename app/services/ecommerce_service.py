from . import CatalogoService, CompraService, PagoService, InventarioService, SagaBuilder
from app import cache

catalogo_service = CatalogoService()
compra_service = CompraService()
pago_service = PagoService()
inventario_service = InventarioService()

class EcommerceService():

    def consultar_producto(self, id_producto:int):
        producto = cache.get(f"producto_{id_producto}")
        if producto is None:
            producto = catalogo_service.obtener_producto(id_producto)
            if producto is None:
                return None
            cache.set(f"producto_{id_producto}", producto, timeout=100)
        return producto
    
    # def comprar_producto(data):
    #     response = SagaBuilder()  \
    #     .action(compra_service.comprar,compra_service.borrar_compra) \
    #     .action(pago_service.agregar_pago,pago_service.borrar_pago) \
    #     .action(inventario_service.agregar_stock,inventario_service.borrar_stock) \
    #     .set_data(data) \
    #     .build() \
    #     .execute()

    #     return response