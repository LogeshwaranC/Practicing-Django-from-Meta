from django.http import HttpResponse, HttpResponseNotFound

def handler404(requst,exception):
    return HttpResponse("404")

