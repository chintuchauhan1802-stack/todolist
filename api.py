from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data dictionary acting as a temporary database
items_db = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99}
]

# Route to get all items (GET)
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({"items": items_db}), 200

# Route to get a single item by ID (GET)
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in items_db if i["id"] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

# Route to add a new item (POST)
@app.route('/api/items', methods=['POST'])
def create_item():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
        
    data = request.get_json()
    
    # Simple validation
    if "name" not in data or "price" not in data:
        return jsonify({"error": "Missing required fields: 'name' or 'price'"}), 400

    new_item = {
        "id": len(items_db) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    items_db.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    # Starts the local development server on http://127.0.0.1:5000
    app.run(debug=True)
