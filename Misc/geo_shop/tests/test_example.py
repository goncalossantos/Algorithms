# -*- coding: utf-8 -*-
import pytest
from flask import current_app


@pytest.fixture()
def base_payload():
    # Almost exactly Witting-Renner
    return {
        'total_products': 10,
        'lat': 59.43265972650577,
        'lng': 18.06061237898499,
        'radius': 10000,
    }


@pytest.fixture(params=["a", "a,b,c"])
def base_payload_with_bad_tags(request, base_payload):
    base_payload.update({'tags': request.param})
    return base_payload


@pytest.fixture(params=["underwear", "underwear,clothes"])
def base_payload_with_good_tags(request, base_payload):
    # Witting-Renner
    base_payload.update({'tags': request.param})
    return base_payload


@pytest.fixture(params=[-1, 0])
def invalid_total_products_payload(request, base_payload):

    base_payload['total_products'] = request.param
    return base_payload


@pytest.fixture(params=[1, 5])
def base_payload_different_total_products(request, base_payload):
    base_payload['total_products'] = request.param
    return base_payload


@pytest.fixture(params=[(91, 0), (-91, 0), (0, 181), (0, -181)])
def invalid_coords_payload(request, base_payload):
    base_payload['lat'] = request.param[0]
    base_payload['lng'] = request.param[1]
    return base_payload


@pytest.fixture(params=[0])
def empty_range_payload(request, base_payload):
    base_payload['radius'] = request.param
    return base_payload


@pytest.fixture(params=[-1])
def invalid_radius_payload(request, base_payload):
    base_payload['radius'] = request.param
    return base_payload


@pytest.fixture(params=['total_products', 'lat', 'lng', 'radius'])
def missing_params_payload(request, base_payload):
    del base_payload[request.param]
    return base_payload


class TestSearch(object):

    URI = '/search'

    def check_response(self, get, params, code):
        # Main method that sends the request and tests the status code of the response
        response = get(self.URI, query_string=params)
        assert response.status_code == code
        return response.json

    def test_invalid_total_products(self, get, invalid_total_products_payload):
        self.check_response(get, invalid_total_products_payload, 400)

    def test_invalid_radius(self, get, invalid_radius_payload):
        self.check_response(get, invalid_radius_payload, 400)

    def test_invalid_coords(self, get, invalid_coords_payload):
        self.check_response(get, invalid_coords_payload, 400)

    def test_missing_params(self, get, missing_params_payload):
        self.check_response(get, missing_params_payload, 400)

    def test_empty_range(self, get, empty_range_payload):

        response = self.check_response(get, empty_range_payload, 200)
        assert 'products' in response
        assert len(response['products']) == 0

    def test_total_products(self, get, base_payload_different_total_products):

        response = self.check_response(
            get, base_payload_different_total_products, 200)

        assert 'products' in response
        assert len(response['products']) == base_payload_different_total_products[
            'total_products']

    def test_bad_tag(self, get, base_payload_with_bad_tags):
        response = self.check_response(get, base_payload_with_bad_tags, 200)
        assert 'products' in response
        assert len(response['products']) == 0

    def test_result_is_sorted(self, get, base_payload):

        response = self.check_response(get, base_payload, 200)
        assert 'products' in response
        p = response['products']
        assert all(p[i]['popularity'] >= p[i + 1]['popularity']
                   for i in xrange(len(p) - 1))

    def test_good_tags(self, get, base_payload_with_good_tags):

        tag_list = base_payload_with_good_tags['tags'].split(',')
        response = self.check_response(get, base_payload_with_good_tags, 200)
        assert 'products' in response
        assert len(response['products']) == base_payload_with_good_tags[
            'total_products']
        for product in response['products']:
            shop = next(
                p.shop for p in current_app.csv_static_data.products if p.id == product['id'])
            assert not set(tag_list).isdisjoint(set(shop.tags))

    def test_format(self, get, base_payload):

        response = self.check_response(get, base_payload, 200)
        assert 'products' in response
        product_list = response['products']
        for product in product_list:
            # Check keys
            assert set(product.keys()) == {'id', 'popularity', 'quantity', 'shop', 'title'}
            assert set(product['shop'].keys()) == {'name', 'lat', 'lng'}
            # Sheck main data types
            assert isinstance(product['shop']['lat'], float)
            assert isinstance(product['shop']['lng'], float)
            assert isinstance(product['popularity'], float)
            assert isinstance(product['quantity'], int)
            assert isinstance(product['title'], unicode)
