from flask import Flask # type: ignore
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'MrKevin'


if __name__ == "__main__":
    app.run()
