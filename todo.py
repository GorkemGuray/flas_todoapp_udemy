import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db_path = os.path.join(os.path.dirname(__file__), 'todo.db').replace("\\","/")
db_uri = 'sqlite:///{}'.format(db_path)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)




class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean, default=False)

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)
