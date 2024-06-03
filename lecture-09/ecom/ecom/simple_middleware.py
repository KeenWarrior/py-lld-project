def simple_middleware(get_response):

    print("Setup first middleware")

    def middleware(request):

        # forward going area
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        # backward going area

        return response

    return middleware


def another_middleware(get_response):

    print("Setup second middleware")

    def middleware(request):

        # forward going area
        print("This is another middleware before view")
        response = get_response(request)
        print("This is another middleware after view")
        # backward going area

        return response

    return middleware



# def sum(a, b):
#     return a + b
#
# def divide(a, b):
#     return a/b
#
# def perform_ops(op, a, b):
#     return op(a, b)
#
#
# perform_ops(divide, 2, 3)
