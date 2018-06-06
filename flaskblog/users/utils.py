import random, uuid
import os
from PIL import Image
from flask import current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = int(random.random() * 1000000)
    f_name, f_ext = os.path.splitext(form_picture.filename) # can use _, instead of f_name since will not use it.
    picture_fn = str(random_hex) + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    # output_size = (125, 125)
    # i = Image.open(form_picture)
    # i.thumbnail(output_size)
    form_picture.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Passord Reset Requet', sender='noreply@demo.com', recipients=[user.email])
    msg.body = '''to reset your passowrd, visit the following link:
    {url_for('users.reset_token', token={}, _external=True)}
    If you did not make this request then please ignore this email and no changes will be made.  
    '''.format(token)

