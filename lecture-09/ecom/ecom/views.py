from django.http import HttpResponse


def say_hello(request):
    print("This is within view")
    return HttpResponse("Hello from Scaler")
