from flask import Flask, request, jsonify

app = Flask("Employee API")

employees = [
    {"id": 1, "Employee_Name": "Rahul", "age": 25, "Phone_no": "9876543210", "Department": "IT"},
    {"id": 2, "Employee_Name": "Anita", "age": 30, "Phone_no": "9123456780", "Department": "HR"}
]

# Get all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    if len(employees) != 0:
        return jsonify({"Result": employees})
    else:
        return jsonify({"Error": "No employees found"}), 404


# Get employee by ID
@app.route('/employee/<int:eid>', methods=['GET'])
def get_employee(eid):
    emp = next((e for e in employees if e["id"] == eid), None)

    if emp:
        return jsonify(emp)
    else:
        return jsonify({"Error": f"Employee not found with id={eid}"}), 404


# Add employee
@app.route('/employee/add', methods=['POST'])
def add_employee():
    data = request.get_json()

    new_emp = {
        "id": len(employees) + 1,
        "Employee_Name": data["Employee_Name"],
        "age": data["age"],
        "Phone_no": data["Phone_no"],
        "Department": data["Department"]
    }

    employees.append(new_emp)

    return jsonify({
        "Message": "Employee added successfully",
        "Employee": new_emp
    })


# Update employee
@app.route('/employee/edit/<int:eid>', methods=['PUT'])
def update_employee(eid):

    emp = next((e for e in employees if e["id"] == eid), None)

    if emp:
        data = request.get_json()
        emp.update(data)
        return jsonify({"Updated Employee": emp})
    else:
        return jsonify({"Error": f"Employee not found with id={eid}"}), 404


# Delete employee
@app.route('/employee/remove/<int:eid>', methods=['DELETE'])
def delete_employee(eid):

    emp = next((e for e in employees if e["id"] == eid), None)

    if emp:
        employees.remove(emp)
        return jsonify({"Message": f"Employee removed with id={eid}"})
    else:
        return jsonify({"Error": f"Employee not found with id={eid}"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5050)