from flask import Flask
from pages import pages  # Changed from home to pages

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session management

app.register_blueprint(pages, url_prefix="/home")  # Still using /home as the URL prefix

if __name__ == '__main__':
    app.run(debug=True, port=8000)
