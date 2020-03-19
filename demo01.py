from flask import Flask

app = Flask(__name__,static_folder="test")


@app.route("/")
def index():
    return "hello world"

@app.route("/hello01")
def hello():
    return "你好"

if __name__ == '__main__':
    app.run() ##启动Flask
