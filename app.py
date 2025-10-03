# Main application file for the Flask web server.
# This code defines a simple web endpoint.

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    This function handles requests to the root URL ('/') and returns a simple greeting.
    """
    return "Hello, World! from CI/CD with GitHub Actions!"

if __name__ == '__main__':
    # This block runs the application on a local development server.
    # It listens on all available network interfaces (0.0.0.0).
    app.run(host='0.0.0.0', port=5000)
