import pytest
import nginx_utils

#https://docs.pytest.org/en/7.1.x/reference/fixtures.html#fixture

@pytest.fixture(scope="class")
def nginx_json():
    """ 
    Load NGINX configuration from use case 1.
    """
    nu = nginx_utils.NginxUtils()
    return nu.crossplane_output('nginx/use_case_1/nginx.conf', True)


@pytest.fixture(scope="class")
def nginx_json_faulty():
    """ 
    Load NGINX configuration from use case 2.
    """
    nu = nginx_utils.NginxUtils()
    return nu.crossplane_output('nginx/use_case_2/nginx.conf', True)


@pytest.fixture(scope="class")
def locations(nginx_json):
    """ 
    Extract locations from NGINX configuration.
    """
    nu = nginx_utils.NginxUtils()
    locations = nu.get_locations('root', nginx_json)
    return locations