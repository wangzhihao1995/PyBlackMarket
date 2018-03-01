from flask import jsonify
from black_market.api._bp import create_blueprint
from black_market.api.utils import get_downstream, post_downstream, put_downstream

bp = create_blueprint('wechat', __name__, url_prefix='/wechat')


@bp.route('/jscode2session', methods=['GET'])
def jscode2session():
    """JScode to Session"""
    r = get_downstream("/api/wechat/jscode2session")
    return jsonify(r.json()), r.status_code


@bp.route('/check_session', methods=['GET'])
def check_session():
    """Check Session"""
    r = get_downstream("/api/wechat/check_session")
    return jsonify(r.json()), r.status_code


@bp.route('/user', methods=['GET'])
def get_wechat_user():
    r = get_downstream("/api/wechat/user")
    return jsonify(r.json()), r.status_code


@bp.route('/user', methods=['POST'])
def create_wechat_user():
    r = post_downstream("/api/wechat/user")
    return jsonify(r.json()), r.status_code


@bp.route('/user', methods=['PUT'])
def update_wechat_user():
    r = put_downstream("/api/wechat/user")
    return jsonify(r.json()), r.status_code
