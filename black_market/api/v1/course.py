from flask import jsonify
from .._bp import create_blueprint
from black_market.api.utils import get_downstream

bp = create_blueprint('course', __name__, url_prefix='/course')


@bp.route('/', methods=['GET'])
def get_courses():
    r = get_downstream("/api/course")
    return jsonify(r.json()), r.status_code


@bp.route('/<int:course_id>', methods=['GET'])
def get_course(course_id):
    r = get_downstream("/api/course/" + course_id)
    return jsonify(r.json()), r.status_code
