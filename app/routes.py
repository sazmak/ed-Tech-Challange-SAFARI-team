from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Book, db

# 1. Сначала СОЗДАЕМ объект Blueprint
main = Blueprint('main', __name__)

# 2. Только ПОТОМ используем его в декораторах
@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        category = request.form.get('category')
        link = request.form.get('link')
        
        if title and author and link:
            new_book = Book(title=title, author=author, category=category, link=link)
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('main.index'))
    
    # Логика поиска
    search_query = request.args.get('search')
    if search_query:
        books = Book.query.filter(Book.title.contains(search_query) | Book.author.contains(search_query)).all()
    else:
        books = Book.query.all()
        
    return render_template('index.html', books=books)