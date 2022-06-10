import subprocess
import json


class NginxUtils:

    def crossplane_output(self, filename):
        """ 
        Convert nginx.conf file specified in the parameter 'filename' to a JSON object using 'crossplane' application.
        """   
        result = subprocess.run(['crossplane', 'parse', '--indent=4', '--include-comments', filename], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)


    def get_location(self, uri, locations):
        """ 
        Search a location using uri value.
        """   
        loc = ''
        for i in range(len(locations)):
            if len(locations[i]["args"]) == 1:
                loc = locations[i]["args"][0]
            else:
                loc = locations[i]["args"][1]
            if uri == loc:
                return locations[i]
        return None


    def copyData(self, source, target):
        """ 
        Copy all elements from 'source' object into 'target' object.
        """    
        for i in range(len(source)):
            target.append( source[i] )

    
    def get_locations(self, name, data):
        """ 
        Get list of locations from NGINX JSON object.
        """   
        my_list = []

        if isinstance(data, list):
            for i in range(len(data)):
                if isinstance(data[i], dict) :
                     self.copyData( self.get_locations(name + ' ' + str(i), data[i]) , my_list)
                else: 
                    if isinstance(data[i], list):
                        self.copyData( self.get_locations(str(i), data[i]) , my_list)

        if isinstance(data, dict):
            for key in data.keys():
                if isinstance(data[key], list):
                    self.copyData( self.get_locations(key, data[key]) , my_list)
                else:
                    if isinstance(data[key], dict):
                        self.copyData( self.get_locations(key, data[key]) , my_list)
                    else:
                        #print(key)
                        if (key == "directive") and (data[key] == "location"):
                            my_list.append(data)
                            #print(data)

        return my_list
    