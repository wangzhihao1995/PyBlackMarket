from flask import jsonify

from .._bp import create_blueprint
from black_market.api.utils import get_downstream, post_downstream, put_downstream

bp = create_blueprint('goods.post', __name__, url_prefix='/goods/post')


@bp.route('/', methods=['GET'])
def get_goods_post_list():
    r = get_downstream("/api/goods/post")
    return jsonify(r.json()), r.status_code


@bp.route('/', methods=['POST'])
def create_new_goods_post():
    r = post_downstream("/api/goods/post")
    return jsonify(r.json()), r.status_code


@bp.route('/mine', methods=['GET'])
def get_my_goods_post():
    r = get_downstream("/api/goods/post/mine")
    return jsonify(r.json()), r.status_code


@bp.route('/<int:goods_post_id>', methods=['GET'])
def get_goods_post_by_id(goods_post_id):
    r = get_downstream("/api/goods/post/" + str(goods_post_id))
    return jsonify(r.json()), r.status_code


@bp.route('/<int:goods_post_id>', methods=['PUT'])
def update_goods_post_by_id(goods_post_id):
    r = put_downstream("/api/goods/post/" + str(goods_post_id))
    return jsonify(r.json()), r.status_code


@bp.route('/viewcount', methods=['GET'])
def get_remaining_view_contact_count():
    r = get_downstream("/api/goods/post/viewcount")
    return jsonify(r.json()), r.status_code


@bp.route('/viewcount', methods=['PUT'])
def view_goods_post_contact():
    r = put_downstream("/api/goods/post/viewcount")
    return jsonify(r.json()), r.status_code
