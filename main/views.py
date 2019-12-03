from . import main
from app.requests import getquotes
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from .forms import BlogForm,CommentForm,UpdateProfile,UpdateBlog,SubscriberForm
from ..models import Blogs,Comments,Users,Subscriber
from .. import db,photos
from ..email import mail_message

@main.route('/',methods = ['GET','POST'])
def index():
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data
        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()
        mail_message("You have been subscribed to blog log","email/welcome_subscriber",new_subscriber.email,subscriber=new_subscriber)

    quotesapp = getquotes()
    blogs = Blogs.viewblogs()
    return render_template('index.html',quotesapp = quotesapp,blogs = blogs,SubscriberForm= form)

@main.route('/viewblogs/all')
def viewblogs():
    blogs = Blogs.viewblogs()

    return render_template('viewblogs.html',blogs = blogs)

@main.route('/new_blog',methods = ['GET','POST'])
@login_required
def new_blog():

    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        author = form.author.data

        new_blog = Blogs(title = title,blog = blog,author = author,user = current_user.username)
        new_blog.save_blog()
        subscribers=Subscriber.query.all()
        for subscriber in subscribers:
            mail_message("New Blog Post","email/new_post",subscriber.email,blog = new_blog)
        return redirect(url_for('main.index'))


    return render_template('new_blog.html' , BlogForm = form)

@main.route('/blog,<id>')
@login_required
def blog(id):
    blog = Blogs.query.filter_by(id = id).first()

    comment = Comments.view_comments()
    return render_template('index.html',blog = blog,comment = comment)

@main.route('/comment/<int:id>' , methods = ['GET' , 'POST'])
def comment(id):
    # blog = Blogs.query.filter_by(id = id).first()
    form = CommentForm()
    comment = Comments.view_comments(blog_id = id)
    

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(comment = comment,user = current_user.username,blog_id = id)
        new_comment.save_comments()
        return redirect(url_for('.comment',id = id ))

    return render_template('comment.html',commentForm = form,comment = comment)

@main.route('/user/<usernam>')
def profile(usernam):
    user = Users.query.filter_by(username = usernam).first()
    blogs = Blogs.get_user_blogs(user.username)



    if user is None:
        abort(404)

    return render_template('profile/profile.html',user = user,blogs = blogs)

@main.route('/user/<usernam>/update',methods =['GET','POST'])
@login_required
def update_profile(usernam):
    user = Users.query.filter_by(username = usernam).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',usernam = user.username))

    return render_template('profile/update.html',form = form)

@main.route('/delete/<id>',methods = ['GET','POST'])
@login_required
def delete_blog(id):
    blog = Blogs.query.filter_by(id = id).first()
    
    Blogs.delete_blog(blog)

    return redirect(url_for('main.profile',usernam = current_user.username))

@main.route('/delete_comment/<id>',methods = ['GET','POST'])
@login_required
def delete_comment(id):
    comment = Comments.query.filter_by(id = id).first()


    Comments.delete_comment(comment)
    return redirect (url_for('main.comment',usernam = current_user.username,id = id))

@main.route('/update/<id>',methods = ['GET','POST'])
@login_required
def update_blog(id):
    blog = Blogs.query.filter_by(id = id).first()

    form = UpdateBlog()

    if form.validate_on_submit():
        blog.title = form.title.data
        blog.blog = form.blog.data

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('main.profile',usernam = current_user.username))

    return render_template('profile/updateblog.html',form = form)

@main.route('/user/<usernam>/update/pic',methods = ['POST'])
@login_required
def update_pic(usernam):
    user = Users.query.filter_by(username = usernam).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',usernam = usernam))

