from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    shell_data = {
        "db": db,
        "User": User,
        "Post": Post
    }
    return shell_data
