import os

from flask import Flask

def create_app():
    app = Flask(__name__)

    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
