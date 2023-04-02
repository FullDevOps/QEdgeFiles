from django.http import HttpResponse


# create your views here
def welcome_view(request):
    print('This line added by view function names welcome_view...!!!')
    return HttpResponse('<h1>Custom Middleware Demo</h1> <hr />')
