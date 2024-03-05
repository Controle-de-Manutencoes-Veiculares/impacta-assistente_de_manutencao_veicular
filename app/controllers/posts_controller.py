from flask import render_template
from app.models.post import Post

class PostsController:
    def show(self, id):
        post = Post.qquery.get(id)
        return render_template('posts/show.html', post=post)