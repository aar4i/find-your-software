import os
from flask import Flask
from flaskext.mysql import MySQL

# Create MySQL object (will be initialized later)
mysql = MySQL()

def create_app(test_config=None):
    """Application Factory for Flask application"""
    
    # Create Flask application
    app = Flask(__name__, instance_relative_config=True)
    
    # BD configuration
    app.config.from_mapping(
        SECRET_KEY='dev',
        MYSQL_DATABASE_HOST='localhost',
        MYSQL_DATABASE_PORT=3306,
        MYSQL_DATABASE_USER='root',
        MYSQL_DATABASE_PASSWORD='',
        MYSQL_DATABASE_DB='find_your_software',
        MYSQL_DATABASE_CHARSET='utf8mb4'
    )
    
    if test_config is None:
        # Load config from instance/config.py (overrides defaults)
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load test config
        app.config.from_mapping(test_config)
    
    # Create instance folder if it doesn't exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Initialize MySQL DB
    mysql.init_app(app)

    # Register blueprints
    from . import routes
    app.register_blueprint(routes.bp)
    
    
    return app