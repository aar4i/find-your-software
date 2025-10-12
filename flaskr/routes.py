from flask import Blueprint, request, jsonify, render_template
from flaskr import mysql
from flaskr.haystack_search import recommender

bp = Blueprint('main', __name__)

# Flag to track Haystack initialization
_haystack_initialized = False

def ensure_haystack_initialized():
    """Initialize Haystack on first request (for lazy initialization)"""
    global _haystack_initialized
    if not _haystack_initialized:
        recommender.initialize(mysql)
        _haystack_initialized = True

@bp.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@bp.route('/health')
def health():
    """Health check endpoint for monitoring"""
    return {'status': 'ok'}

@bp.route('/recommend', methods=['POST'])
def recommend():
    """
    Main recommendation endpoint using Haystack AI search.
    Expects JSON body with 'query' field.
    """
    try:
        # Initialize Haystack on first request
        ensure_haystack_initialized()
        
        # Get JSON data
        data = request.get_json()
        
        if not data or 'query' not in data:
            return jsonify({
                "success": False,
                "message": "Missing 'query' field in request body"
            }), 400
        
        query = data['query'].strip()
        
        if not query:
            return jsonify({
                "success": False,
                "message": "Query cannot be empty"
            }), 400
        
        # Get recommendation from Haystack
        from flaskr.haystack_search import recommender
        result = recommender.recommend(query)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Internal server error: {str(e)}"
        }), 500


@bp.route('/software')
def get_software():
    """Get all software entries from database"""
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