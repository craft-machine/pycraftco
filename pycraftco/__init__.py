from sgqlc.operation import Operation
from sgqlc.endpoint.http import HTTPEndpoint
from craft_api_schema import craft_api_schema as schema


API_KEY = "***API KEY***"
HEADERS = {"x-craft-api-key": API_KEY}
API_ENDPOINT = "https://api.craft.co/v1/query"


if __name__ == '__main__':
    op = Operation(schema.Query)
    company = op.company(domain='facebook.com')
    company.locations.city()
    company.locations.hq()
    endpoint = HTTPEndpoint(API_ENDPOINT, HEADERS)
    data = endpoint(op)
    print(data)
