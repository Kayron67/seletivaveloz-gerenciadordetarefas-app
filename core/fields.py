from rest_framework.relations import HyperlinkedIdentityField

class HyperlinkedNestedIdentityField(HyperlinkedIdentityField):

    def __init__(self, view_name=None, **kwargs):
        self.parent_lookup_kwargs = kwargs.pop('parent_lookup_kwargs', {})
        super().__init__(view_name, **kwargs)

    def get_url(self, obj, view_name, request, format):
        kwargs = {
            self.lookup_field:getattr(obj, self.lookup_field)
        }
    
        for parent_lookup_kwargs, parent_lookup_field in self.parent_lookup_kwargs.items():
            parent_obj = obj
            for field in parent_lookup_field.split('.'):
                parent_obj = getattr(parent_obj, field)
            kwargs[parent_lookup_kwargs] = parent_obj

        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)