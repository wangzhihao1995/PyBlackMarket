from flask import Blueprint, jsonify

from black_market.model.exceptions import BlackMarketError

bp = Blueprint('errors', __name__)

@bp.app_errorhandler(BlackMarketError)
def handle_biz_error(error):
    return jsonify(error=dict(message=error.message, code=error.code, type="BlackMarketError")), error.http_status_code
