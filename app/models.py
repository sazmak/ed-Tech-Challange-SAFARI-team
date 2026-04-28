from app import db
from datetime import datetime

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # Название
    author = db.Column(db.String(100), nullable=False) # Автор
    category = db.Column(db.String(50))                # Категория (Математика, ИТ и т.д.)
    link = db.Column(db.String(200), nullable=False)   # Ссылка на скачивание/просмотр
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Book {self.title}>"