from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

class Quote:
    '''
    Quote class that defines quote objects
    '''

    def __init__(self,id,quote,author):
        self.id = id
        self.quote = quote
        self.author = author

class Users(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String,unique = True)
    pass_secure =db.Column(db.String)


    @property
    def password(self):
        raise AttributeError('Password attribute cannot be read')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))


class Blogs(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    blog = db.Column(db.String)
    author = db.Column(db.String)
    user = db.Column(db.String)


    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def viewblogs(cls):
        blogs = Blogs.query.all()
        return blogs

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    user = db.Column(db.String)
    blog_id = db.Column(db.Integer)

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def view_comments(cls,blog_id):
        comments = Comments.query.filter_by(blog_id = blog_id).all()
        return comments



    

    