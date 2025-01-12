from flask import jsonify, request, Blueprint
from .models import Book
from app import create_app, db

app = Blueprint('app', __name__)

@app.route('/')
def index():
    return "Flask and MySQL are connected!"

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    if not all(key in data for key in ('title', 'author', 'year', 'genre')):
        return jsonify({'error': 'Missing data'}), 400

    book = Book(title=data['title'], author=data['author'], year=data['year'], genre=data['genre'])
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.year = data.get('year', book.year)
    book.genre = data.get('genre', book.genre)
    db.session.commit()
    return jsonify(book.to_dict()), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'}), 200
