import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
import os
from PIL import Image
import datetime


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    picture = sqlalchemy.Column(sqlalchemy.String,
                                index=True, unique=True, nullable=True)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def avatar(self, us, db, filename, size=200):
        img = Image.open(f'static/user_pic/{filename}')

        # Получаем размеры изображения
        width, height = img.size

        # Вычисляем размер квадрата для обрезки
        min_dim = min(width, height)
        left = (width - min_dim) // 2
        top = (height - min_dim) // 2
        right = (width + min_dim) // 2
        bottom = (height + min_dim) // 2

        # Обрезаем изображение по середине
        img_cropped = img.crop((left, top, right, bottom))

        # Уменьшаем размер изображения
        img_resized = img_cropped.resize((size, size))

        # Сохраняем результат
        us.picture = f'static/user_pic/{filename}'
        os.remove(f'static/user_pic/{filename}')
        img_resized.save(f'static/user_pic/{filename}', quality=95)
        db.commit()
