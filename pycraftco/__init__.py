import os

from sgqlc.operation import Operation
from sgqlc.endpoint.http import HTTPEndpoint

from pycraftco.craft_api_schema import craft_api_schema as schema


def get_company(query_callback, api_key,
                id=None, duns=None, name_contains=None, domain=None,
                api_endpoint="https://api.craft.co/v1/query"):
    if not any(a for a in [id, duns, name_contains, domain]):
        raise ValueError('One of duns, name_contains or domain should be passed.')

    op = Operation(schema.Query)
    company = op.company(id=id, duns=duns, name_contains=name_contains, domain=domain)

    query_callback(company)

    endpoint = HTTPEndpoint(api_endpoint, {"x-craft-api-key": api_key})
    data = endpoint(op)

    if 'errors' in data:
        errors = data['errors']
        raise ApiError(f'API return errors: {errors}')

    found_company = (op + data).company
    if found_company:
        return found_company


class ApiError(Exception):
    pass


if __name__ == '__main__':
    def query(company):
        company.display_name()
        company.locations.city()
        company.locations.hq()

    c = get_company(query, name_contains='Facebook', api_key=os.environ['API_KEY'])
    print(c)
