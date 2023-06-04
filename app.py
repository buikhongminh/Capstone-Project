from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Udacity', name='Viet Bui')

app.run(host='0.0.0.0', port=81)