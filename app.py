from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import simplejson
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:////tmp/test.db')
db = SQLAlchemy(app)


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(80), unique=True)

    def __init__(self, tweet):
        self.tweet = tweet

    def __repr__(self):
        return '<tweet %r>' % self.tweet

@app.route('/post/<txt>')
def postalo(txt):
    t = Tweet(txt)
    db.session.add(t)
    db.session.commit()
    return "ok"

@app.route('/list')
def listalo():
    return simplejson.dumps([str(x) for x in Tweet.query.all()])

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8080)

