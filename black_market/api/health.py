from flask import Blueprint, jsonify
from black_market.api.utils import normal_jsonify, get_downstream

bp = Blueprint('health', __name__, url_prefix='/health')


@bp.route('', methods=['GET'])
def health():
    return normal_jsonify({'status': 'ok'})


@bp.route('/downstream', methods=['GET'])
def downstream_health():
    r = get_downstream("/health")
    return jsonify(r.json()), r.status_code
