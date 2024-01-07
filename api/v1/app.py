#!/usr/bin/python3
"""Initializes and configures a Flask app"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """Ensures that the storage is properly closed"""
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """Handles 404 errors"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
