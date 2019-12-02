from flask import jsonify, make_response
from app.api import bp


@bp.route('/test', methods=['GET'])
def test_connection():
    return make_response(jsonify({'is_called': True}))
