from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://lidl:CoolPassword233@localhost:3306/lidl-test-db' \
                                 '?auth_plugin=mysql_native_password'
db = SQLAlchemy(app)
ma = Marshmallow(app)

if __name__ == '__main__':
    from controller.garland_controller import init_routs

    init_routs(api)
    db.create_all()
    app.run(debug=True)
