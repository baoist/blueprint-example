from flask import Flask
from views.index import index

app = Flask(__name__)

app.register_blueprint(index)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
