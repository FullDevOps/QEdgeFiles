class ExecutionFlowMiddleware(object):
    def __init__(self, get_response):
        print("init() is executed only once..!!")
        self.get_response = get_response

    def __call__(self, request):
        print('This line added at pre-processing of request')
        response = self.get_response(request)
        print('This line added at post-processing of request')
        return response
