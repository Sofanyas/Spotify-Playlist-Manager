import os
from flask import Blueprint, redirect, session, url_for, request
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

# Create a Blueprint for the main routes
main = Blueprint('main', __name__)

# Route to initiate the login process with Spotify
@main.route('/login')
def login():
    sp_oauth = SpotifyOAuth(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
        scope='user-read-private user-read-email playlist-modify-public playlist-modify-private'
    )
    return redirect(sp_oauth.get_authorize_url())

# Callback route that Spotify redirects to after authentication
@main.route('/callback')
def callback():
    sp_oauth = SpotifyOAuth(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI')
    )

    # Retrieve the authorization code from the query parameters
    code = request.args.get('code')

    # Use the authorization code to get the access token
    token_info = sp_oauth.get_access_token(code)

    if token_info:
        # Store the access token securely in the session
        session['token_info'] = token_info
        return redirect(url_for('main.user'))
    else:
        return "Authentication failed", 400


# Route to display user information after authentication
@main.route('/user')
def user():
    token_info = session.get('token_info', {})
    
    if not token_info:
        return redirect(url_for('main.login'))

    sp = Spotify(auth=token_info['access_token'])
    user_data = sp.current_user()
    
    return f"Hello, {user_data['display_name']}!"
