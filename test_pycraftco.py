import pytest

from unittest.mock import Mock, patch

from pycraftco import get_company, ApiError
from pycraftco.craft_api_schema import Company


def test_no_search_args():
    with pytest.raises(ValueError):
        get_company(_query_callback, 'test_key')


def test_company_not_found():
    endpoint_mock = Mock(return_value={'data': {'company': None}})
    with patch('pycraftco.HTTPEndpoint', return_value=endpoint_mock):
        assert get_company(_query_callback, 'test_key', domain='example.org') is None


def test_incorrect_api_key():
    endpoint_mock = Mock(return_value={
        'data': None, 'errors': [{'message': 'HTTP Error 401: Unauthorized'}]
    })
    with patch('pycraftco.HTTPEndpoint', return_value=endpoint_mock):
        with pytest.raises(ApiError):
            assert get_company(_query_callback, 'test_key', domain='example.org') is None


def test_correct_request():
    endpoint_mock = Mock(return_value={
        'data': {
            'company': {
                'displayName': 'Facebook',
                'locations': [
                    {'city': 'Warsaw', 'hq': False},
                    {'city': 'Vancouver', 'hq': False},
                    {'city': 'Toronto', 'hq': False}
                ]
            }
        }
    })
    with patch('pycraftco.HTTPEndpoint', return_value=endpoint_mock):
        assert get_company(_query_callback, 'test_key', domain='example.org') is not None


def _query_callback(company):
    company.display_name()
    company.locations.city()
    company.locations.hq()
