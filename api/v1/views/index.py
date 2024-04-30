#!/usr/bin/python3

from flask import jsonify
from api.v1.views import app_views  # Import the blueprint

# Define a route handler for the /status endpoint within the blueprint
@app_views.route('/status')
def status():
    """Returns a JSON response indicating the API status."""
    return jsonify({"status": "OK"})