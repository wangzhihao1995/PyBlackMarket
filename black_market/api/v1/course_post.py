from flask import jsonify
from .._bp import create_blueprint
from black_market.api.utils import get_downstream, post_downstream, put_downstream

bp = create_blueprint('course.post', __name__, url_prefix='/course/post')


@bp.route('/', methods=['GET'])
def get_course_post_list():
    r = get_downstream("/api/course/post")
    return jsonify(r.json()), r.status_code


@bp.route('/', methods=['POST'])
def create_new_course_post():
    r = post_downstream("/api/course/post")
    return jsonify(r.json()), r.status_code


@bp.route('/mine', methods=['GET'])
def get_my_course_post():
    r = get_downstream("/api/course/post/mine")
    return jsonify(r.json()), r.status_code


@bp.route('/<int:course_post_id>', methods=['GET'])
def get_course_post_by_id(course_post_id):
    r = get_downstream("/api/course/post/" + course_post_id)
    return jsonify(r.json()), r.status_code


@bp.route('/<int:course_post_id>', methods=['PUT'])
def update_course_post_by_id(course_post_id):
    r = put_downstream("/api/course/post/" + course_post_id)
    return jsonify(r.json()), r.status_code
