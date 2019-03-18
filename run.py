# coding:utf-8

# from app import app

from flask import Flask
app = Flask(__name__, static_url_path='')


from app.dept import dept

from app.user import user


app.register_blueprint(user, url_prefix='/user')

app.register_blueprint(dept, url_prefix='/dept')

if __name__ == '__main__':

    app.run()