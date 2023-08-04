from flask import Blueprint, jsonify

bp = Blueprint('api', __name__)

@bp.route('/', methods=['GET'])
def apiHome():
    return jsonify({ 'status': 'OK', 'message': 'Welcome to Software Effort Estimation API' })

@bp.route('/healthcheck', methods=['GET'])
def apiHealthcheck():
    return jsonify({ 'status': 'OK', 'message': 'API is working!' })