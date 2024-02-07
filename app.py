from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('email')
    return f'Dane przesłane: Imię - {name}, E-Mail - {email}'

if __name__ == '__main__':
    app.run(debug=True)
