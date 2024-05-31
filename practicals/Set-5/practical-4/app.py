from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data (replace with your actual data source)
items = [f"Item {i}" for i in range(1, 101)]


# Route that supports pagination
@app.route("/items", methods=["GET"])
def get_items():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_items = items[start_index:end_index]
    return jsonify(
        {
            "items": paginated_items,
            "page": page,
            "per_page": per_page,
            "total_items": len(items),
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
