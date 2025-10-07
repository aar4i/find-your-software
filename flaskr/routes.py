from flask import Blueprint
from flaskr import mysql

# Create Blueprint
bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    """Main endpoint - API info"""
    return {
        'message': 'Find Your Software API',
        'status': 'running',
        'version': '1.0'
    }


@bp.route('/health')
def health():
    """Health check endpoint for monitoring"""
    return {'status': 'ok'}


@bp.route('/recommend', methods=['POST'])
def recommend():
    """Main recommendation endpoint - will implement with Haystack later"""
    return {
        'message': 'Recommendation endpoint - coming soon',
        'status': 'not_implemented'
    }, 501