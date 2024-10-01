import os
from flask import Flask, session
from routes import main  # Import the main blueprint from routes.py

# Load environment variables directly
app = Flask(__name__)

# Set the secret key for session management
app.secret_key = os.getenv('SECRET_KEY', 'your_default_secret_key')  # Make sure to set this in Render

# Register the main blueprint to make the routes available
app.register_blueprint(main)

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5024)
