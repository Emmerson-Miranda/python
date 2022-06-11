import nginx_utils

class TestClassNginxLocations:

    def test_locations_counter(self, locations):
        """ 
        Verifying the number of locations.
        """
        assert len(locations) == 5


    def test_configuration_without_errors(self, nginx_json):
        """ 
        Checking the configuration does not have errors.
        """
        assert len(nginx_json['errors']) == 0


    def test_configuration_with_errors(self, nginx_json_faulty):
        """ 
        Verifying errors
        """
        assert len(nginx_json_faulty['errors']) == 1
        assert nginx_json_faulty['errors'][0]['error'] == "[Errno 2] No such file or directory: 'nginx/use_case_2/mime.types'"


    def test_location_none(self, locations):
        """ 
        Verifying that a path does not exist. 
        """
        nu = nginx_utils.NginxUtils()
        loc = nu.get_location('/any/missing/path', locations)
        assert loc == None


    def test_access_token_location_present(self, locations):
        """ 
        Verifying that the location exist.
        """
        nu = nginx_utils.NginxUtils()
        loc = nu.get_location('/_business/abc', locations) 

        assert loc != None
        assert loc["block"][0]["directive"] == "internal"
