from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/next')
def hello_world1():
  return 'Hello, World Next Page'

@app.route("/test")
def test():
  return "This is my first application running"

@app.route("/test2")
def test2():
  data =  request.args.get('x')
  return "These is my data {}".format(data)


if __name__ == '__main__':
       app.run(debug=True)