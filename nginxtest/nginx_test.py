import nginx_utils

class TestClassNginxLocations:

    def test_locations_counter(self, locations):
        """ 
        Test the transformation using default values  
        """
        assert len(locations) == 5


    def test_location_none(self, locations):
        """ 
        Test the transformation using default values  
        """
        nu = nginx_utils.NginxUtils()
        loc = nu.get_location('/any/missing/path', locations)
        assert loc == None


    def test_access_token_location_present(self, locations):
        """ 
        Test the transformation using default values  
        """
        nu = nginx_utils.NginxUtils()
        loc = nu.get_location('/_business/abc', locations) 

        assert loc != None
        assert loc["block"][0]["directive"] == "internal"
