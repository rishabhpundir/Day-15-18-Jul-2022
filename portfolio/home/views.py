from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("This is a index page.")
    context = {'name':'Rishabh Pundir', 'occupation':'Web Developer Intern'}
    return render(request, 'index.html', context)
    
def about(request):
    return render(request, 'about.html')
    
def login(request):
    return render(request, 'login.html')
    
def contact(request):
    return render(request, 'contact.html')
