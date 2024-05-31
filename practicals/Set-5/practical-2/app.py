from flask import Flask, jsonify, request

app = Flask(__name__)
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"},
]


@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)

    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404


@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    new_book = {"id": len(books) + 1, "title": data["title"], "author": data["author"]}
    books.append(new_book)
    return jsonify(new_book), 201


@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        data = request.get_json()
        book["title"] = data["title"]
        book["author"] = data["author"]
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404


@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"result": True})


if __name__ == "__main__":
    app.run(debug=True)
