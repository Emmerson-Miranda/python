import pytest
import nginx_utils

#https://docs.pytest.org/en/7.1.x/reference/fixtures.html#fixture

@pytest.fixture(scope="class")
def nginx_json():
    """ 
    Convert nginx.conf file specified in the parameter 'filename' to a JSON object using 'crossplane' application.
    """
    print('\n---  Fixture nginx json object ---\n')
    nu = nginx_utils.NginxUtils()
    return nu.crossplane_output('nginx/nginx.conf')


@pytest.fixture(scope="class")
def locations(nginx_json):
    print('\n---  Fixture locations from nginx json object ---\n')
    nu = nginx_utils.NginxUtils()
    locations = nu.get_locations('root', nginx_json)
    return locations