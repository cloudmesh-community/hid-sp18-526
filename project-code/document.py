import yaml

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

    def add_apis(self, *args):
        """ Add APIs, by yaml file
        Args:
            *args - each argument supplied should lead to a .yml document in /documents
        """
        
        apis = {}
        
        # load yaml files
        for arg in args:
            with open('documents/' + arg + '.yml', 'r') as f:
                api = yaml.load(f)
                for key, value in api.items():
                    if key not in apis:
                        apis[key] = value
                    else:
                        apis[key].update(value)

        for key, value in apis.items():
            setattr(self, key, value)
            
    def to_dict(self):
        return self.__dict__
