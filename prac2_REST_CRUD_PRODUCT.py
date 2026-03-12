from flask import Flask, request, jsonify

app = Flask("Product API")

products = [
    {"id": 1, "Product_Name": "Milk", "Quantity": 20, "Expiry_date": "2026-04-01"},
    {"id": 2, "Product_Name": "Bread", "Quantity": 15, "Expiry_date": "2026-03-20"}
]

# GET all products
@app.route('/products', methods=['GET'])
def get_products():
    if len(products) != 0:
        return jsonify({"Result": products})
    else:
        return jsonify({"Error": "No products found"}), 404


# GET single product by id
@app.route('/product/<int:p_id>', methods=['GET'])
def get_product(p_id):
    product = next((p for p in products if p["id"] == p_id), None)

    if product:
        return jsonify(product)
    else:
        return jsonify({"Error": f"Product not found with id={p_id}"}), 404


# ADD new product
@app.route('/product/add', methods=['POST'])
def add_product():
    data = request.get_json()

    new_product = {
        "id": len(products) + 1,
        "Product_Name": data["Product_Name"],
        "Quantity": data["Quantity"],
        "Expiry_date": data["Expiry_date"]
    }

    products.append(new_product)

    return jsonify({
        "Message": "Product added successfully",
        "New Product": new_product,
        "All Products": products
    })


# UPDATE product
@app.route('/product/edit/<int:p_id>', methods=['PUT'])
def update_product(p_id):

    product = next((p for p in products if p["id"] == p_id), None)

    if product:
        data = request.get_json()
        product.update(data)
        return jsonify({"Updated Product": product})
    else:
        return jsonify({"Error": f"Product not found with id={p_id}"}), 404


# DELETE product
@app.route('/product/remove/<int:p_id>', methods=['DELETE'])
def delete_product(p_id):

    product = next((p for p in products if p["id"] == p_id), None)

    if product:
        products.remove(product)
        return jsonify({"Message": f"Product removed with id={p_id}"})
    else:
        return jsonify({"Error": f"Product not found with id={p_id}"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5050)