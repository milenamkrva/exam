from flask import render_template
from app.models import db, Article, Category

def index_page(category_id=None):
    categories = Category.query.all()
    if category_id:
        articles = Article.query.filter_by(category_id=category_id).order_by(Article.create_date.desc()).all()
    else:
        articles = Article.query.order_by(Article.create_date.desc()).all()
    return render_template('index.html', categories=categories, articles=articles)

def article_page(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article.html', article=article)