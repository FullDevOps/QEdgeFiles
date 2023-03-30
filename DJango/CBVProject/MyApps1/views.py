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


from django.views.generic import TemplateView


class TemplateCBV(TemplateView):
    template_name = "MyApps1/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # this two lines are inportant

        context['name'] = 'Sai'
        context['age'] = 23
        context['height'] = 6.2
        return context


# ListView
from MyApps1.models import Book
from django.views.generic import ListView


# Create your views here.
class BookListView(ListView):
    model = Book  # book_list=Book.objects.all();
