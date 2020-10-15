import copy

from flask_marshmallow.schema import Schema
from flask import request, make_response

from model.garland import Garland, GarlandSchema
from app import db
from flask_restful import Resource

garland_schema = GarlandSchema()
garlands_schema = GarlandSchema(many=True)


class GarlandsApi(Resource):

    def get(self):
        garlands = Garland.query.all()
        return garlands_schema.jsonify(garlands)

    def post(self):
        body = request.get_json()
        garland = Garland(**body)

        db.session.add(garland)
        db.session.commit()

        return garland_schema.jsonify(garland)


class GarlandApi(Resource):

    def put(self, garland_id):
        body = request.get_json()
        garland = Garland.query.get(garland_id)
        old_garland = None

        if garland is not None:
            old_garland = copy.deepcopy(garland)
            garland.set_fields(**body)
            db.session.commit()

        return error_handler(old_garland, garland_schema)

    def delete(self, garland_id):
        garland = Garland.query.get(garland_id)

        if garland is not None:
            db.session.delete(garland)
            db.session.commit()

        return error_handler(garland, garland_schema)

    def get(self, garland_id):
        garland = Garland.query.get(garland_id)
        return error_handler(garland, garland_schema)


def error_handler(object_to_check, return_schema: Schema):
    response, status = (return_schema.jsonify(object_to_check), 200) \
        if object_to_check is not None \
        else ("", 404)
    return make_response(response, status)


def init_routs(api):
    api.add_resource(GarlandsApi, '/garlands')
    api.add_resource(GarlandApi, '/garlands/<garland_id>')
