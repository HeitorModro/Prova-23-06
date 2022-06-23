from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)

class graus(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  graus = db.Column(db.String())

@app.route('/create', methods=['POST'])
def create():
 graus = request.form.get('graus')
 new_graus = graus( graus=graus )
 db.session.add(new_graus)
 db.session.commit()
 return redirect('/')

@app.route('/')
def index():
  new_graus = graus.query.all()
  return render_template('index.html', new_graus = new_graus)

@app.route('/converter')
def converter():
    return render_template('temperatura.html')
  
if __name__ == '__main__':
  db.create_all()
  app.run(host='0.0.0.0', port=81)