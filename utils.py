from __future__ import print_function
__author__ = 'javier'


def custom_resource(self, function, request, **kwargs):
    self.method_check(request, allowed=['get'])
    self.is_authenticated(request)
    self.throttle_check(request)

    output = function(**kwargs)
    print(output)
    # try:
    # except Exception as failure:
    #     return self.create_response(request, { 'status' : 'failure', 'reason' : failure.message })

    self.log_throttled_access(request)
    return self.create_response(request, output)