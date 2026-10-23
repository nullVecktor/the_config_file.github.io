
from flask import Blueprint, current_app, render_template

from .posts import list_posts

main = Blueprint("main", __name__)


@main.get("/")
def dashboard():
    posts = list_posts(current_app.config["POSTS_DIR"])

    return render_template(
        "dashboard.html",
        posts=posts,
    )
