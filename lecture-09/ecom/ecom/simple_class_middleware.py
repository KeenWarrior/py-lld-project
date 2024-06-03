from django.http import HttpResponse
from ecom.views import EmptyException

class SimpleClassMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # this is before
        print("This is before part of class based middleware")
        response = self.get_response(request)
        # this is after
        print("This is after part of class based middleware")
        return response

    def process_exception(self, request, exception):

        if type(exception) is EmptyException:
            print(str(exception))
            return HttpResponse("This is empty")

        return None

def sum(a, b):
    return a + b

sum(10, b = 10)


