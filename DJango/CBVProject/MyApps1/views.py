from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
class HelloWorldView(View):
    def get(self, request):
        ss = '''<h1>Hello from Class-Bassed-View</h1>
        <hr />
        <h2>Response given for get-method from client</h2>
        <h3>Have a nice day..!!</h3>
        <hr />
        <h4>***ALL THE BEST***</h4>
        '''
        return HttpResponse(ss)
