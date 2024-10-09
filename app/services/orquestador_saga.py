import requests


class OrquestadorSaga:

    def add_compra(self,data):
        data_compra = data.get('compra')
        r = requests.post('http://127.0.0.1:3002/api/v1/compras', json=data_compra)
        if r.status_code == 201:
            print("Compra exitosa")
            data['compra_key'] = r.json().get('data').get('id')
            return self.add_pago(data)
        else:
            return r.json().get('data'), "Fallo en request_compra", r.status_code

    def add_pago(self,data):
        data_pago = data.get('pago')
        r = requests.post('http://127.0.0.1:3003/api/v1/pagos', json=data_pago)
        if r.status_code == 201:
            print("Pago exitoso")
            data['pago_key'] = r.json().get('data').get('id')
            return self.add_stock(data)
        else:
            self.compensate_compra(data)
            return r.json().get('data'), "Fallo en request_pago", r.status_code
    
    def add_stock(self,data):
        data_stock = data.get('stock')
        r = requests.post('http://127.0.0.1:3004/api/v1/inventario', json=data_stock)
        if r.status_code == 201:
            print("Stock exitoso")
            data['stock_key'] = r.json().get('data').get('id')
            return None, 'El producto fue comprado con exito', r.status_code
        else:
            self.compensate_pago(data)
            return r.json().get('data'), "Fallo en request_stock", r.status_code
        
    def compensate_compra(self,data):
        compra_key = data.get('compra_key')
        print(f"compensate_compra: {compra_key}")
        requests.delete(f'http://127.0.0.1:3002/api/v1/compras/{compra_key}')

    def compensate_pago(self,data):
        pago_key = data.get('pago_key')
        requests.delete(f'http://127.0.0.1:3003/api/v1/pagos/{pago_key}')
        self.compensate_compra(data)

    def compensate_stock(self,data):
        stock_key = data.get('stock_key')
        requests.delete(f'http://127.0.0.1:3004/api/v1/inventario/{stock_key}')
        self.compensate_compra(data)