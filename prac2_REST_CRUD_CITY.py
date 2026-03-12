from flask import Flask, request, jsonify

app = Flask("City API")

cities = [
    {"id": 1, "City_Name": "Mumbai", "District_Name": "Mumbai Suburban", "Population": 12400000},
    {"id": 2, "City_Name": "Pune", "District_Name": "Pune", "Population": 7400000}
]

# Get all cities
@app.route('/cities', methods=['GET'])
def get_cities():
    if len(cities) != 0:
        return jsonify({"Result": cities})
    else:
        return jsonify({"Error": "No cities found"}), 404


# Get city by ID
@app.route('/city/<int:cid>', methods=['GET'])
def get_city(cid):
    city = next((c for c in cities if c["id"] == cid), None)

    if city:
        return jsonify(city)
    else:
        return jsonify({"Error": f"City not found with id={cid}"}), 404


# Add new city
@app.route('/city/add', methods=['POST'])
def add_city():
    data = request.get_json()

    new_city = {
        "id": len(cities) + 1,
        "City_Name": data["City_Name"],
        "District_Name": data["District_Name"],
        "Population": data["Population"]
    }

    cities.append(new_city)

    return jsonify({
        "Message": "City added successfully",
        "City": new_city
    })


# Update city
@app.route('/city/edit/<int:cid>', methods=['PUT'])
def update_city(cid):

    city = next((c for c in cities if c["id"] == cid), None)

    if city:
        data = request.get_json()
        city.update(data)
        return jsonify({"Updated City": city})
    else:
        return jsonify({"Error": f"City not found with id={cid}"}), 404


# Delete city
@app.route('/city/remove/<int:cid>', methods=['DELETE'])
def delete_city(cid):

    city = next((c for c in cities if c["id"] == cid), None)

    if city:
        cities.remove(city)
        return jsonify({"Message": f"City removed with id={cid}"})
    else:
        return jsonify({"Error": f"City not found with id={cid}"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5050)