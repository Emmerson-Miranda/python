import json
import crossplane


class NginxUtils:

    def crossplane_output(self, filename, create_temporal_file):
        """ 
        Convert nginx.conf file specified in the parameter 'filename' to a JSON object using 'crossplane' application.
        """   
        result = crossplane.parse(filename)
        if create_temporal_file:
            f = open(filename + ".json", "w")
            f.write(json.dumps(result))
            f.close()
        return result


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
    