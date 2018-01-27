from flask import Flask
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def home():
    """
    在访问 httt://127.0.0.1:5000 的时候，在浏览器显示标题 "Hello World!"
    """
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run()
