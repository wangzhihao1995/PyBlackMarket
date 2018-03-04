from flask import jsonify
from black_market.api._bp import create_blueprint
from black_market.api.utils import get_downstream, post_downstream, put_downstream

bp = create_blueprint('student', __name__, url_prefix='/student')


@bp.route('/', methods=['GET'])
def get_current_student():
    r = get_downstream("/api/student")
    return jsonify(r.json()), r.status_code


@bp.route('/', methods=['POST'])
def create_student():
    r = post_downstream("/api/student")
    return jsonify(r.json()), r.status_code


@bp.route('/', methods=['PUT'])
def update_student():
    r = put_downstream("/api/student")
    return jsonify(r.json()), r.status_code


@bp.route('/post', methods=['GET'])
def get_current_student_post_list():
    r = get_downstream("/api/student/post")
    return jsonify(r.json()), r.status_code


@bp.route('/register', methods=['POST'])
def send_register_code():
    r = post_downstream("/api/student/register")
    return jsonify(r.json()), r.status_code


@bp.route('/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    r = get_downstream("/api/student/" + str(student_id))
    return jsonify(r.json()), r.status_code


@bp.route('/<int:student_id>/post', methods=['GET'])
def get_student_post_list_by_student_id(student_id):
    r = get_downstream("/api/student/" + str(student_id) + "/post")
    return jsonify(r.json()), r.status_code


@bp.route('/share/profile/<int:student_id>', methods=['GET'])
def get_student_share_profile(student_id):
    r = get_downstream("/api/student/share/profile/" + str(student_id))
    return jsonify(r.json()), r.status_code
