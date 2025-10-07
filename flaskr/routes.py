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

@bp.route('/software') 
def get_software():
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT id, name, description, category FROM software')
        software_list = cursor.fetchall()
        cursor.close()
        
        result = []
        for software in software_list:
            result.append({
                'id': software[0],
                'name': software[1],
                'description': software[2],
                'category': software[3]
            })
        
        return {'count': len(result), 'software': result}
    except Exception as e:
        return {'error': str(e)}, 500