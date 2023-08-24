from django.shortcuts import render
from django.http import HttpResponse 
from .forms import Inputforms
from django.views.generic.edit import CreateView   


# Create your views here.
def view(request):
    return HttpResponse("'string' Its worked ")

def test(request):
    path = request.path
    method = request.method
    content = '''
<center><h2>Testing Request Response Objects</h2>
<p>Request Path :  {}</p>
<p>Request Method : {}</p></center>
'''.format(path, method)
    return HttpResponse(content)

def form_view(request):
    form = Inputforms()
    if request.method == 'POST':
        form = Inputforms(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

   


    