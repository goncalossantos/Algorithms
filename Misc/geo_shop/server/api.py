# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, jsonify, request

from .forms import SearchForm
from .search_query import SearchQuery

api = Blueprint('api', __name__)


def data_path(filename):
    data_path = current_app.config['DATA_PATH']
    return u"%s/%s" % (data_path, filename)


def error(message, code):
    response = jsonify(message)
    response.status_code = code
    return response


@api.route('/search', methods=['GET'])
def search():

    form = SearchForm(request.args)
    if form.validate():
        data = current_app.csv_static_data
        sq = SearchQuery(data, form)
        return jsonify({'products': list(sq.apply())})
    else:
        return error(form.errors, 400)
