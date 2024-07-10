from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import db, Category, Article


class ArticleModelView(ModelView):
    column_list = ('id', 'category', 'title', 'description', 'author', 'create_date', 'photo_small', 'photo_large')

admin = Admin()
admin.add_view(ModelView(Category, db.session, name='Category', endpoint='category_admin'))
admin.add_view(ArticleModelView(Article, db.session, name='Article', endpoint='article_admin'))
