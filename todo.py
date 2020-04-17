import os
from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

db_path = os.path.join(os.path.dirname(__file__), 'todo.db').replace("\\","/")
db_uri = 'sqlite:///{}'.format(db_path)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

@app.route('/')
def index():
    todos=Todo.query.all()
    return render_template('index.html',todos=todos)

@app.route('/add', methods=['POST'])
def addTodo():
    title = request.form.get("title")
    newTodo = Todo(title=title, complete=False)
    db.session.add(newTodo)
    db.session.commit()

    return  redirect(url_for('index'))

@app.route('/complete/<string:id>')
def completeTodo(id):
    todo =  Todo.query.filter_by(id=id).first()
    todo.complete = not todo.complete
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def deleteTodo(id):
    Todo.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for('index'))



class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)
