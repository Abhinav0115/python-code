'''
Expore the Flask module and create a web server using Flask and python. 

Flask: 
    - Flask is a python module that allows you to create web servers. 
    - It is a micro web framework written in Python.
    - It is classified as a microframework because it does not require particular tools or libraries.
    - It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.
    - Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine.
    - It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

'''

from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    s = "Hello, guys! Welcome to the world of Flask."
    return s

if __name__ == "__main__":
    app.run()

