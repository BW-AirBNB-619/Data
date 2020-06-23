from flask import Flask

def create_app():
    app = Flask(__name__)
    return app


@app.route("/")
def index():
    return f"Hello World!"
    

if __name__ == '__main__':
    my_app=create_app()
    my_app.run(debug=True)