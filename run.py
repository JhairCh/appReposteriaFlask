
# from flask import Flask

# from .extensions import appbuilder, db


# def create_app() -> Flask:
#     app = Flask(__name__)
#     app.config.from_object("config")

#     db.init_app(app)

#     with app.app_context():
#         appbuilder.init_app(app, db.session)

#         from . import models
#         from . import views

#     return app

from app import app
 
if __name__ == "__main__":
    app.run(debug=True)