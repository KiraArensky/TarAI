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

    def avatar(self, us, db, filename):
        im = Image.open(f'static/user_pic/{filename}')
        img_width, img_height = im.size
        img = im.crop(((img_width - 200) // 2,
                       (img_height - 200) // 2,
                       (img_width + 200) // 2,
                       (img_height + 200) // 2))
        us.picture = f'static/user_pic/{filename}'
        os.remove(f'static/user_pic/{filename}')
        img.save(f'static/user_pic/{filename}', quality=95)
        db.commit()
