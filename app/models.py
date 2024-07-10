from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __str__(self):
        return self.name

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('articles', lazy=True))
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(64), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    photo_small = db.Column(db.String(128))
    photo_large = db.Column(db.String(128))


    def __repr__(self):
        return f'<Article {self.title}>'


