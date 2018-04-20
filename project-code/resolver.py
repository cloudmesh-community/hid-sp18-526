from connexion.resolver import Resolver

class CMResolver(Resolver):
    """This resolver imports the original resolver and allows passing a dict of endpoints.
    
    *** taken from the original connexion resolver 
        @https://github.com/zalando/connexion/blob/master/connexion/resolver.py
    """

    def __init__(self, controller_dispatch = {}, default_module_name = 'controllers', collection_endpoint_name = 'search'):
        """
        Args:
            default_module_name
            collection_endpoint_name
        """
        
        Resolver.__init__(self)
        self.controller_dispatch = controller_dispatch
        self.default_module_name = default_module_name
        self.collection_endpoint_name = collection_endpoint_name

    # unchanged
    def resolve_operation_id(self, operation):
        """
        Resolves the operationId using REST semantics unless explicitly configured in the spec
        :type operation: connexion.operation.Operation
        """
        if operation.operation.get('operationId'):
            return Resolver.resolve_operation_id(self, operation)

        return self.resolve_operation_with_dispatch(operation)

    def resolve_operation_with_dispatch(self, operation):
        """Returns endpoint based on parent/child dispatch
        
        <default controller>.<api name>.<child name>.<method>
        ie. controller.services.list.get
        """
        
        path = operation.path[1:]

        return '{}.{}.{}.{}'.format(self.default_module_name, self.controller_dispatch[path], path, operation.method)
