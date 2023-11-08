from flask import redirect
from .extentions import login
from .models import Users

@login.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@login.unauthorized_handler
def unauthorized():
    return redirect("/login")