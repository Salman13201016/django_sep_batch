from django.http import HttpResponse

def index(request):
    return HttpResponse("this is a demo index function")
def index2(request):
    return HttpResponse("this is a demo index2 function")

def index1(request):
    return HttpResponse("this is a demo root index function")