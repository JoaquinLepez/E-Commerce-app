from flask import Blueprint, request
import requests

e_commerce = Blueprint('e_commerce', __name__)


@e_commerce.route('/e_commerce', methods=['GET'])
def index():
    return "Hello, World!"

@e_commerce.route('/e_commerce/prueba', methods=['GET'])
def prueba():
    r = requests.get('http://127.0.0.1:3001/api/v1/productos/producto')
    if r.status_code == 200:
        return r.json()
    else:
        return 'Error'
    