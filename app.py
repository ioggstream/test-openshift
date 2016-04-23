from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import simplejson
import os
from random import randint

app = Flask(__name__)
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://test:test@{MYSQL_SERVICE_HOST}:{MYSQL_SERVICE_PORT}/test".format(**os.environ)
except KeyError:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(80), unique=True)

    def __init__(self, tweet):
        self.tweet = tweet

    def __repr__(self):
        return '<tweet %r>' % self.tweet

    def __str__(self):
        return self.tweet


@app.route('/post/<txt>')
def postalo(txt):
    t = Tweet(txt)
    db.session.add(t)
    db.session.commit()
    return "ok"


@app.route('/list')
def listalo():
    return simplejson.dumps([str(x) for x in Tweet.query.all()])


@app.route('/')
def help():
    return """
    <html><body>
    Connected to {db}.
    <a href="/list">List posts</a><br>
    <a href="/post/{random}">Submit post</a><br>
    </body></html>
    """.format(
        db=db.session,
        random=randint(1,1000)
    )


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8080, host='0.0.0.0')

