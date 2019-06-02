from ..models import User, Comments, Post
from . import main
from flask import render_template, request, redirect, url_for, abort
from .forms import UpdateProfile, DisplayPost, CommentForm
from flask_login import login_required, current_user
from .. import db, photos

@main.route("/", methods=['GET', 'POST'])
def index():
    form = DisplayPost()
    if form.validate_on_submit():
        post = form.text.data

        # Updated post
        new_post = Post(post=post, user=current_user)

        # save pitch method
        new_post.save_post()
     
    posts = Post.query.all()
    title = "Home"
    return render_template('index.html', title=title, post_form=form, posts=posts)  

@main.route('/post/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    post = Post.query.filter_by(id=id).first()
    form = CommentForm()
    comment = Comments.query.filter_by(post_id=id).all()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(comment=comment, user_id=current_user.id, post=post)
        new_comment.save_comment()
        return redirect(url_for('main.new_comment', id=post.id))
    
    title = "COMMENTS"   
    return render_template('comments.html', comment=comment, comment_form=form, title=title, post=post)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile_page.html", user=user)

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)