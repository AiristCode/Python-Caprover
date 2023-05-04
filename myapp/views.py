from django.http import HttpResponse

def hello(request):
    return HttpResponse("<p>Customer Experience Team</p>")
