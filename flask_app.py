
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/asw')
def hello_from_me():
    return 'Hello from me'

@app.route("/hello/<name>")
def hello_person(name):
    html = """
    <h1>
    Hello {}!
    </h1>
    <p>
    Here's a picture of a kitten.  Awww...
    </p>
    <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())


@app.route("/test")
def template_test():
    return render_template('template.html')

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
