# Spotify-Playlist-Manager
Requirements gathering list for Spotify playlist-combining application:

### 1. **User Authentication:**
   - **Spotify Login Integration:**
     - Allow users to log in using their Spotify account.
     - Use Spotify’s OAuth 2.0 for authentication.
     - Ensure access tokens are securely stored and managed.
     - Handle session expiration and token refresh.

### 2. **Access to Spotify Data:**
   - **Playlist Retrieval:**
     - Fetch the user’s playlists from Spotify.
     - Display playlist names, metadata (total songs, duration, etc.), and song details (name, artist, album, etc.).
   - **Permissions:**
     - Request the necessary permissions (playlist-read-private, playlist-modify-public, playlist-modify-private).

### 3. **Playlist Selection:**
   - **Multiple Playlist Selection:**
     - Allow users to select multiple playlists they want to combine.
     - Provide a clear UI for selecting and viewing the playlists.
     
### 4. **Song Filtering:**
   - **Filter by Song Name:**
     - Option to search and filter out specific songs by name before combining.
   - **Filter by Artist:**
     - Allow users to filter out songs by specific artists.
   - **Filter by Album:**
     - Allow filtering out songs from specific albums.

### 5. **Combining Playlists:**
   - **Combine Playlists into Existing Playlist:**
     - After filtering, allow users to combine the selected playlists into an existing playlist.
     - Ensure the selected playlist is updated without affecting the original source playlists.
   - **Create New Playlist:**
     - Provide an option to combine the filtered playlists into a new playlist.
     - Leave the original playlists unchanged.
   - **Handle Duplicates:**
     - Offer options to either skip, overwrite, or add duplicates when combining songs.

### 6. **Playlist Management:**
   - **Playlist Naming:**
     - Allow users to name new playlists when combining.
   - **Metadata:**
     - Display playlist metadata (number of tracks, total duration, etc.).
     - Allow editing of playlist description and settings.

### 7. **User Interface & Experience:**
   - **Intuitive UI:**
     - Easy-to-use interface for selecting and filtering songs.
     - Drag-and-drop functionality for playlist management.
     - Clear buttons for combining or creating new playlists.
   - **Progress Indicator:**
     - Show progress when filtering or combining large playlists.

### 8. **Error Handling:**
   - **Invalid Playlist/Track Handling:**
     - Ensure appropriate error messages if playlists or songs are unavailable.
   - **Network Issues:**
     - Handle network errors and Spotify API failures gracefully.
     
### 9. **Backend:**
   - **Spotify API Integration:**
     - Use Spotify Web API to fetch playlists, add or remove tracks, and create new playlists.
   - **Database (Optional):**
     - Store user preferences, playlist data (for caching), or song filtering options locally or in the cloud.

### 10. **Testing & Security:**
   - **Testing:**
     - Ensure all Spotify API endpoints work as expected.
     - Test for edge cases like missing playlists, invalid access tokens, etc.
   - **Security:**
     - Secure user data and tokens.
     - Follow best practices for OAuth and API security.
     
### 11. **Deployment & Hosting:**
   - **Hosting Environment:**
     - Choose a cloud service (e.g., AWS, Google Cloud) or use a platform like Heroku.
   - **Scalability:**
     - Plan for scaling if the app grows in user base or API calls.

### 12. **Optional Features (Future Enhancements):**
   - **Playlist Analytics:**
     - Provide users with statistics like the most frequent artist or genre.
   - **Collaborative Playlist:**
     - Allow users to collaborate on playlist combinations with friends.
   - **Social Sharing:**
     - Allow users to share combined playlists directly from the app.
   - **Machine Learning Suggestions:**
     - Suggest songs to add based on user preferences and Spotify’s recommendation API.

This should cover all the major aspects for building the application.

# List of tools and technologies needed to build the Spotify playlist-combining application:

### 1. **Programming Languages:**
   - **Python** (recommended for back-end if you’ve been using Flask)
     - You'll use Python to interact with the Spotify API, handle user data, and process playlist combinations.
   - **JavaScript** (for front-end)
     - Used for building the user interface (UI) and managing interactions on the client side.

### 2. **Frameworks & Libraries:**

   **Backend:**
   - **Flask** (Python framework):
     - Lightweight and ideal for building RESTful APIs to interact with Spotify's API.
   - **Spotipy** (Python library):
     - A lightweight Python library that simplifies working with the Spotify Web API.
   - **SQLAlchemy**:
     - For managing any database-related operations (if you decide to store data locally).
   - **Requests**:
     - For making HTTP requests to the Spotify API.
   
   **Frontend:**
   - **React** (JavaScript framework):
     - A popular front-end library for building interactive user interfaces, making it easier to manage dynamic elements (playlist selection, filtering).
   - **Axios** (HTTP client):
     - For making asynchronous requests from your React front-end to the Flask backend.
   - **Bootstrap** (optional):
     - For styling the UI, creating buttons, forms, and other components easily.

### 3. **Spotify API:**
   - **Spotify Developer Dashboard**:
     - Register your app here to get your client ID and secret for OAuth authentication.
   - **Spotify Web API**:
     - The core API used to retrieve playlists, tracks, and manage user data. Key endpoints:
       - `/me/playlists`: Get user playlists.
       - `/playlists/{playlist_id}/tracks`: Get or add tracks to a playlist.
       - `/users/{user_id}/playlists`: Create a new playlist.

### 4. **Authentication:**
   - **OAuth 2.0**:
     - Spotify uses OAuth 2.0 for authentication and authorization. You'll need to integrate it to allow users to log in and grant access to their Spotify data.
   - **Flask-Dance** (optional):
     - A Flask extension for OAuth that simplifies Spotify authentication.

### 5. **Databases (Optional):**
   - **SQLite** (for local storage):
     - A lightweight database that could be used to store cached playlist data, user preferences, etc.
   - **PostgreSQL** (if scaling):
     - A more robust database option if you plan to host and scale the app.

### 6. **Version Control:**
   - **Git**:
     - Version control system to track changes in your code and collaborate with others.
   - **GitHub/GitLab**:
     - For hosting your code repositories and enabling collaboration.

### 7. **Development Tools:**
   - **Postman**:
     - To test Spotify API endpoints and verify responses before integrating into your app.
   - **Visual Studio Code**:
     - A popular code editor with great support for both Python and JavaScript, as well as debugging tools.

### 8. **Deployment:**
   - **Heroku** (for deploying your Flask app):
     - Easy to set up and deploy Python apps with a free tier for testing.
   - **AWS** (for more robust infrastructure):
     - If you want more control and scalability, AWS services like EC2 or Lambda are good for hosting.
   - **Netlify** or **Vercel** (for front-end deployment):
     - Great for deploying static sites (like React) with easy integration to GitHub.
   
### 9. **Testing:**
   - **PyTest** (for back-end):
     - A simple framework to write and run tests on your Flask code.
   - **Jest** or **Mocha** (for front-end):
     - JavaScript testing frameworks to write unit and integration tests for your React components.

### 10. **Other Tools:**
   - **Docker** (optional but recommended):
     - Containerize your Flask and React apps for easier deployment and consistent environments.
   - **CI/CD Tools** (e.g., **GitHub Actions**, **CircleCI**):
     - Automate the testing and deployment process whenever changes are pushed to your repository.

# step-by-step **Plan of Action** for building Spotify playlist-combining application:

### 1. **Project Setup**
   - **Timeline: 1 day**
   - **Objective**: Set up your project structure and get the initial tools ready.
   - **Steps**:
     - Install the necessary tools: Flask, React, Spotipy, Requests, Axios, SQLite.
     - Create your Git repository and set up version control with GitHub or GitLab.
     - Set up a virtual environment in Python for Flask dependencies (`venv`).
     - Initialize a React app for the front-end interface using `create-react-app`.
     - Set up Spotify Developer Dashboard and create your app to obtain `Client ID` and `Client Secret`.

### 2. **Authentication with Spotify (OAuth 2.0)**
   - **Timeline: 1-2 days**
   - **Objective**: Enable users to log in to their Spotify account and give permission to manage their playlists.
   - **Steps**:
     - Implement OAuth 2.0 with Spotify using the Spotipy library or Flask-Dance.
     - Create a login route (`/login`) in Flask to redirect users to the Spotify login page.
     - Handle the callback after authentication and store the access token securely (you can use session or tokens).
     - Test user login and token retrieval using Postman to confirm authentication works.

### 3. **Retrieve User Playlists**
   - **Timeline: 1 day**
   - **Objective**: Fetch playlists from the logged-in user's Spotify account.
   - **Steps**:
     - Set up a `/playlists` endpoint in Flask to call the Spotify Web API to retrieve user playlists (`/me/playlists` endpoint).
     - Create a function to format and send playlist data (ID, name, tracks, etc.) to the front-end.
     - In React, fetch the playlist data and display it to the user in a dropdown or list format for them to select.

### 4. **Playlist Filtering**
   - **Timeline: 2-3 days**
   - **Objective**: Allow users to filter out songs by name, artist, or album.
   - **Steps**:
     - Add a filter option in the front-end for users to input search terms (song name, artist, album).
     - Create a `/filter` endpoint in Flask to filter playlist tracks based on user input.
     - Use the `/playlists/{playlist_id}/tracks` Spotify endpoint to retrieve all tracks in the selected playlist.
     - Implement filtering logic to remove songs that match the criteria (e.g., remove songs with specific artist names).
     - Update the front-end to show the filtered playlist to the user before combining it with another playlist.

### 5. **Combine Playlists**
   - **Timeline: 2 days**
   - **Objective**: Combine two selected playlists and optionally filter songs before combining.
   - **Steps**:
     - Create a `/combine-playlists` endpoint in Flask.
     - Allow users to select two playlists to combine and handle them in the back-end.
     - Use the `/playlists/{playlist_id}/tracks` endpoint to get the tracks of both playlists.
     - Create logic to merge the tracks while eliminating duplicates (same song in both playlists).
     - Give users the option to either update an existing playlist or create a new playlist.

### 6. **Create New Playlist or Update Existing**
   - **Timeline: 1-2 days**
   - **Objective**: Allow users to create a new playlist or update an existing playlist with the combined tracks.
   - **Steps**:
     - Create a `/create-playlist` endpoint that uses the Spotify API (`/users/{user_id}/playlists`) to create a new playlist.
     - Add a conditional check in the Flask back-end:
       - If the user chooses to combine into a new playlist, call the create playlist API.
       - If the user chooses to update an existing playlist, update the selected playlist using `/playlists/{playlist_id}/tracks` to add tracks.
     - Send a success message and updated playlist details back to the front-end.

### 7. **User Interface Design**
   - **Timeline: 2-3 days**
   - **Objective**: Build the front-end components and user interactions.
   - **Steps**:
     - Build a clean and responsive UI with React for playlist selection, filtering, and combining.
     - Use Bootstrap for styling and layout to create a user-friendly interface.
     - Ensure that the login, playlist selection, and playlist combining processes are seamless.
     - Implement client-side error handling and notifications for invalid inputs or API failures.

### 8. **Testing**
   - **Timeline: 1-2 days**
   - **Objective**: Ensure that all functionality works as expected and there are no critical bugs.
   - **Steps**:
     - Write unit tests for back-end API routes using `PyTest`.
     - Write integration tests for key workflows like playlist retrieval, filtering, and combining.
     - Test OAuth flow to ensure users can log in and retrieve data securely.
     - Use Postman to verify all API responses are working as intended.
     - Test front-end functionality using React testing libraries like Jest.

### 9. **Deployment**
   - **Timeline: 1-2 days**
   - **Objective**: Deploy the application to a production environment.
   - **Steps**:
     - Containerize your app using Docker for consistent environment setup.
     - Deploy the Flask back-end to Heroku or AWS, ensuring that it connects to the Spotify API securely.
     - Deploy the React front-end to Netlify or Vercel.
     - Set up environment variables for Spotify credentials and ensure secure access in the production environment.
     - Verify the deployment by testing the application on live servers.

### 10. **Enhancements (Optional)**
   - **Timeline: Ongoing**
   - **Objective**: Improve the application with additional features.
   - **Steps**:
     - Add pagination for large playlists to improve performance.
     - Implement a search functionality for songs in the Spotify catalog, allowing users to add new tracks to their combined playlist.
     - Integrate caching (using Redis or similar) to avoid repeated calls to the Spotify API.
     - Add user preferences for combining (e.g., exclude certain genres).

---

## Estimated Total Timeline: **10-15 days**

# Progress Log
## Day 1: Working on taks day 1
- Project research/planning
- Project/dependencies set up
- Created React/frontend file by running `npx create-react-app frontend`
- Virtual environment (venv) set up, `.gitignore` set up, and `README.md` set up
- Set up Spotify developer account with Client ID and Client Secret

## Day 2-4: Working on tasks day 2
- Created .env on my local to hold sensitive data like credentials
- Created config.py to map my credentials to keys value pairs in a Config class to be imported into programs
- Created routes.py to handle the routes and logic of each endpoint
- Created app.py to be the main program that executes everything
### Issues
 - I didn't realize my callback url is only hosted locally so the spotify servers can't reach it. Need to host it using AWS or Render.
 - Hosting it on render for now.
 ### Day 4 Update: Still working on day 2 tasks
 - hosted login service on render
 - got rid of .env and config file because I'll be using render's enviormental variables to store all my credentials
 - updated routes.py file beacuse because SpotifyOAuth was trying to prompt the user interactively (via input) to enter the redirected URL, which is not suitable for a web application. Fixed it by manually passing the authorization code from the query parameters