from flask_app import app
from flask_app.controllers import controller_dojo
from flask_app.controllers import controller_ninja


if __name__ == "__main__":
    app.run(debug=True)