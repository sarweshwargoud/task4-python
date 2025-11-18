from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory storage of users (id -> user object)
# Example user object: {"id": 1, "name": "Alice", "email": "a@x.com"}
users = {}
next_id = 1

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "User API is running!"})

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values()))

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/users", methods=["POST"])
def create_user():
    global next_id
    data = request.get_json(force=True, silent=True)
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid payload. 'name' and 'email' required."}), 400

    user = {
        "id": next_id,
        "name": str(data["name"]),
        "email": str(data["email"])
    }
    users[next_id] = user
    next_id += 1
    return jsonify(user), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json(force=True, silent=True)
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    if not data:
        return jsonify({"error": "Invalid payload"}), 400

    # update allowed fields
    name = data.get("name")
    email = data.get("email")
    if name:
        user["name"] = str(name)
    if email:
        user["email"] = str(email)

    users[user_id] = user
    return jsonify(user)

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted = users.pop(user_id)
    return jsonify({"message": "Deleted", "user": deleted})

if __name__ == "__main__":
    # Portable run command — use python app.py
    print("Starting Flask server...")
    app.run(debug=True)
