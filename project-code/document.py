import os
import yaml
import constants

class APIDoc:
    """Class for combining OpenAPI documents
    
    Start by passing the API information to the class
        
    Mandatory Attributes:
        title     
        version
        swagger
        
    Optional Attributes:
        description
        termsOfService
        contact
        license
    """
    
    def __init__(self, title = '', version = '', swagger = '', **kwargs):
        self.info = {'title': title, 'version': version}
        
        setattr(self, 'swagger', swagger)
        
        for key, value in kwargs.items():
            setattr(self, key, value)  

    def set_apis(self, api_list):
        """ Add APIs, by yaml file
        Args:
            api_list - each argument supplied should lead to a yaml document in /documents
            
        Returns:
            dict of {child: parent}
        """
        
        if api_list == 'all':
            api_list = os.listdir('apis')

        apis = {}
        parents = {}
        
        # load yaml files
        for name in api_list:
            with open(constants.API_ROOT + '/' + name + '/' + constants.SPECIFICATION_FILE + '.' + constants.YAML_EXTENSION, 'r') as f:
                api = yaml.load(f)
                for key, value in api.items():
                    
                    # add each key and its parent to parents dict
                    for vkey in value.keys():
                        parents[vkey[1:]] = name
                    
                    if key not in apis:
                        apis[key] = value
                    else:
                        apis[key].update(value)

        for key, value in apis.items():
            setattr(self, key, value)
            
        return parents
            
    def to_dict(self):
        return self.__dict__
        
    def to_yaml(self):
        return yaml.dump(self.__dict__, default_flow_style = False)
