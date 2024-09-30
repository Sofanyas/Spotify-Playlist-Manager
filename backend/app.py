from flask import Flask, session
from config import Config  # Assuming Config contains your app settings
from routes import main  # Import the main blueprint from routes.py

# Create a Flask application instance
app = Flask(__name__)

# Load the configuration from the Config class
app.config.from_object(Config)

# Set the secret key for session management
app.secret_key = 'your_secret_key'  # Make sure to use a secure secret key in production

# Set the Spotify OAuth configuration
app.config['SPOTIPY_CLIENT_ID'] = 'your_client_id'
app.config['SPOTIPY_CLIENT_SECRET'] = 'your_client_secret'
app.config['SPOTIPY_REDIRECT_URI'] = 'http://127.0.0.1:5000/callback'  # Your redirect URI

# Register the main blueprint to make the routes available
app.register_blueprint(main)

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5024)  # Enable debug mode for development

