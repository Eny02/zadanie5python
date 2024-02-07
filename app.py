from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'YOUR_DATABASE_CONNECTION_STRING'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    
    return 'Dane przesłane i zapisane do bazy danych!'

if __name__ == '__main__':
    app.run(debug=True)
