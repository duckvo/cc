#2a
from flask import Flask, Response
import xml.etree.ElementTree as ET

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return "welcome to python web service"

if __name__ == '__main__':
    app.run()

#2b
#book
from flask import Flask, request, jsonify, Response
import xml.etree.ElementTree as Et

app = Flask("Books APP")

books = [
    {"id": 1, "title": "CC & WS", "author": "Dr. XYZ"},
    {"id": 2, "title": "DS", "author": "Dr. LMN"},
]

# Get all books in JSON
@app.route("/books", methods=["GET"])
def get_books():
    if len(books) != 0:
        return jsonify({"Result": books})
    else:
        return jsonify({"Error": "Books not found"}), 400


# Get all books in XML
@app.route('/all_books', methods=['GET'])
def get_all_books():
    root = Et.Element('books')
    for book in books:
        xml_book = Et.SubElement(root, 'book')
        xml_book.set('id', str(book['id']))

        b_title = Et.SubElement(xml_book, 'title')
        b_title.text = book['title']

        b_author = Et.SubElement(xml_book, 'author')
        b_author.text = book['author']

    xml_string = Et.tostring(root)
    return Response(xml_string, mimetype="text/xml")


# Get a specific book by ID
@app.route("/book/<int:b_id>", methods=["GET"])
def get_a_book(b_id):
    book = next((b for b in books if b["id"] == b_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"Error": f"Book not found with id={b_id}"}), 404


# Update a book by ID
@app.route("/book/edit/<int:b_id>", methods=["PUT"])
def update_book(b_id):
    book = next((b for b in books if b["id"] == b_id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({"Error": f"Book not found with id={b_id}"}), 404


# Add a new book
@app.route("/book/add", methods=["POST"])
def add_book():
    data = request.get_json()
    new_book = {"id": len(books) + 1, "title": data["title"], "author": data["author"]}
    books.append(new_book)
    return jsonify({"New added book": new_book, "All Books": books})


# Remove a book by ID
@app.route('/book/remove/<int:bid>', methods=['DELETE'])
def remove_book(bid):
    book = next((b for b in books if b['id'] == bid), None)
    if book:
        books.remove(book)
        return jsonify({"Msg": f"Book removed successfully with id: {bid}"})
    else:
        return jsonify({"Error": f"Book not found with id={bid}"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=2546)
