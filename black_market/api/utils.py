import json
import requests
from flask import jsonify, request

from black_market.model.exceptions import DownstreamConnectionError
from black_market.config import DOWN_STREAM_URL


def normal_jsonify(data=None, err_msg='', status_code=200):
    return jsonify({'data': data, 'errMsg': err_msg}), status_code


def get_downstream(route):
    try:
        r = requests.get(DOWN_STREAM_URL + route, params=request.args, headers=request.headers)
    except requests.exceptions.ConnectionError:
        raise DownstreamConnectionError
    return r


def post_downstream(route):
    try:
        r = requests.post(
            DOWN_STREAM_URL + route, data=json.dumps(request.json), headers=request.headers)
    except requests.exceptions.ConnectionError:
        raise DownstreamConnectionError
    return r


def put_downstream(route):
    try:
        r = requests.put(
            DOWN_STREAM_URL + route, data=json.dumps(request.json), headers=request.headers)
    except requests.exceptions.ConnectionError:
        raise DownstreamConnectionError
    return r
