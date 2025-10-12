import os
from flask import Flask
from flaskext.mysql import MySQL

# Create MySQL object (will be initialized later)
mysql = MySQL()

def create_app(test_config=None):
    """Application Factory for Flask application"""
    
    app = Flask(__name__, instance_relative_config=True)
    
    # Default config (used locally)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MYSQL_DATABASE_HOST=os.getenv('MYSQL_DATABASE_HOST', 'db'),
        MYSQL_DATABASE_PORT=int(os.getenv('MYSQL_DATABASE_PORT', 3306)),
        MYSQL_DATABASE_USER=os.getenv('MYSQL_DATABASE_USER', 'root'),
        MYSQL_DATABASE_PASSWORD=os.getenv('MYSQL_DATABASE_PASSWORD', 'mysecretpassword'),
        MYSQL_DATABASE_DB=os.getenv('MYSQL_DATABASE_DB', 'find_your_software'),
        MYSQL_DATABASE_CHARSET=os.getenv('MYSQL_DATABASE_CHARSET', 'utf8mb4')
    )
    
    if test_config is None:
        # Load config from instance/config.py if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load test config (for testing)
        app.config.from_mapping(test_config)
    
    # Create instance folder if it doesn't exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Initialize MySQL
    mysql.init_app(app)

    # Register routes
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app
