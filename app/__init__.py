from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.admin import admin, ArticleModelView
from app.models import db, migrate, Category, Article
from app.views import index_page, article_page

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)

    app.add_url_rule("/", view_func=index_page)
    app.add_url_rule("/category/<int:category_id>", view_func=index_page)
    app.add_url_rule("/article/<int:article_id>", view_func=article_page)


    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)