#!/usr/bin/python3
"""creating a variable app, which is an instance of flask."""


from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from models import storage
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': '0.0.0.0'}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """an app that handles and calls"""
    if storage is not None:
        storage.close()


@app.errorhandler(404)
def errorhandler(error):
    """404 error handler"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
