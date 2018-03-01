from flask import jsonify
from .._bp import create_blueprint
from black_market.api.utils import post_downstream

bp = create_blueprint('qiniu', __name__, url_prefix='/qiniu')


@bp.route('/token', methods=['POST'])
def get_token():
    r = post_downstream("/api/qiniu/token")
    return jsonify(r.json()), r.status_code


@bp.route('/callback', methods=['POST'])
def callback():
    raise NotImplementedError