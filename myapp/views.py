from django.http import HttpResponse

def hello(request):
    return HttpResponse("<p>Hello Customer Experience Team</p>")
