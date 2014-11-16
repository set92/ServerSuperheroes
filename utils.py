from __future__ import print_function
__author__ = 'javier'


def custom_resource(self, function, request, **kwargs):
    self.method_check(request, allowed=['get'])
    self.is_authenticated(request)
    self.throttle_check(request)

    output = function(**kwargs)

    if isinstance(output, list):
        result = []
        for obj in output:
            bundle = self.build_bundle(obj=obj, request=request)
            result.append(self.full_dehydrate(bundle))

    else:
        bundle = self.build_bundle(obj=output, request=request)
        result = self.full_dehydrate(bundle)

    self.log_throttled_access(request)
    return self.create_response(request, result)