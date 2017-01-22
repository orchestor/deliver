from flask import Flask
from flask import request
from flask import render_template
from deliver import deliver
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my_form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    processed_text = deliver(text)
    return processed_text

if __name__ == '__main__':
    app.run(debug=True)
