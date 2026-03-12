from flask import Flask, request, jsonify

app = Flask("Player APP")

players = [
    {"id": 1, "Player_Name": "Virat Kohli", "Age": 35, "Country": "India", "Runs": 13000},
    {"id": 2, "Player_Name": "Joe Root", "Age": 33, "Country": "England", "Runs": 11500},
]

# Get all players
@app.route("/players", methods=["GET"])
def get_players():
    if len(players) != 0:
        return jsonify({"Players": players})
    else:
        return jsonify({"Error": "No players found"}), 404


# Get player by ID
@app.route("/player/<int:p_id>", methods=["GET"])
def get_player(p_id):
    player = next((p for p in players if p["id"] == p_id), None)

    if player:
        return jsonify(player)
    else:
        return jsonify({"Error": f"Player not found with id={p_id}"}), 404


# Add new player
@app.route("/player/add", methods=["POST"])
def add_player():
    data = request.get_json()

    new_player = {
        "id": len(players) + 1,
        "Player_Name": data["Player_Name"],
        "Age": data["Age"],
        "Country": data["Country"],
        "Runs": data["Runs"]
    }

    players.append(new_player)

    return jsonify({
        "Message": "Player added successfully",
        "Player": new_player
    })


# Update player
@app.route("/player/edit/<int:p_id>", methods=["PUT"])
def update_player(p_id):

    player = next((p for p in players if p["id"] == p_id), None)

    if player:
        data = request.get_json()
        player.update(data)
        return jsonify({"Updated Player": player})
    else:
        return jsonify({"Error": f"Player not found with id={p_id}"}), 404


# Delete player
@app.route("/player/remove/<int:p_id>", methods=["DELETE"])
def remove_player(p_id):

    player = next((p for p in players if p["id"] == p_id), None)

    if player:
        players.remove(player)
        return jsonify({"Message": f"Player removed with id {p_id}"})
    else:
        return jsonify({"Error": f"Player not found with id={p_id}"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=2546)