#!/usr/bin/python3

from flask import Flask
from models import storage
from api.v1.views import app_views

# Create a Flask application instance
app = Flask(__name__)

# Register the blueprint for API v1 views
app.register_blueprint(app_views)

# Close the storage session when the application context tears down
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

# Configure the server based on environment variables
host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
port = int(os.environ.get('HBNB_API_PORT', 5000))

# Run the Flask development server in threaded mode
if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
