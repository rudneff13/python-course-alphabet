from flask import Flask

from .main.routes import main
from .fruits.routes import fruits
from .vegetables.routes import vegetables
from .handler.routes import handler

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(fruits)
app.register_blueprint(vegetables)
app.register_blueprint(handler)


if __name__ == '__main__':
    app.run(debug=True)
