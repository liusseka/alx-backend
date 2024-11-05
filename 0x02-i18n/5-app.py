#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """Return user from the URL parameter login_as"""
    user_id = request.args.get('login_as')
    if user_id is None:
        return None
    user_id = int(user_id)
    return users.get(user_id)

@app.before_request
def before_request():
    """Set user in global context"""
    user = get_user()
    g.user = user

@babel.localeselector
def get_locale():
    """Get locale from user settings or request headers"""
    if g.user and g.user['locale']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Render the index page"""
    return render_template('5-index.html')

if __name__ == "__main__":
    app.run(debug=True)
