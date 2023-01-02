from flask import Flask

from settings import HOST, PORT

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
