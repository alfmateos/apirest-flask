from flask import Flask, jsonify, request
# Importa las listas
from products import products

# Inicializa la aplicacion
app = Flask(__name__)


# Genera la ruta
@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})


@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Products list"})


# Permite obtener cada producto por busqueda
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if
                     product['name'] == product_name]  # busca en cada fila de los productos
    # Busca y devuelve Productos encontrados
    if len(productsFound) > 0:
        return jsonify({"product": productsFound[0]})
        #return productsFound[0]
    return jsonify({"message": "Product not found"})


# adherir productos a nuestra lista
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)  # metodo para agregar nuevos datos
    return jsonify({"message": "Product added Succesfully", "products": products})


# Inicializa el servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)
