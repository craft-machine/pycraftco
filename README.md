## PYCRAFTCO

[![CircleCI](https://circleci.com/gh/craft-machine/pycraftco.svg?style=svg)](https://circleci.com/gh/craft-machine/pycraftco)

**pycraftco** is a Python library that serves as a convenient wrapper for [Craft API](https://api.craft.co/docs/v1).

### Installation

You can install package via `pip`:

    $ pip install pycraftco

### Usage

The snippet below will retrieve name and offices of Facebook. For all available information
please refer to https://api.craft.co/docs/v1/reference/company.doc.html. However, please note
that the API documentation have all fields in camel case but the lib have them
underscore-separated.

```python
from pycraftco import get_company

api_key = 'qfNfdijpFhbhPhA7j2ZxvtEGkfv8DftTtmTEbnWN'

# specify what data to load in the callback
def company_query(company):
    company.display_name()
    company.locations.city()
    company.locations.hq()

# You can use duns, name_constains or domain to search for companies
c = get_company(company_query, name_contains='Facebook', api_key=os.environ['API_KEY'])
```

The code uses the test key that allows access to Facebook data only. Please, visit
https://craft.co/business#business-form to request more permissive key.

### Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/craft-machine/pycraftco .

### License

The pip package is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
