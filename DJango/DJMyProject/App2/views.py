import django.shortcuts
from django.http import HttpResponse
import datetime

def f22(request):
    time = datetime.datetime.now()
    msg = "<h2 style='color:Green;'>Hello User..!!<br /><br />Server Date & Time :: "+str(time)+"</h2><hr/>"
    return HttpResponse(msg)
