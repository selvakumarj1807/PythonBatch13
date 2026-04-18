from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def studentindex(request):
    return render(request, 'studenttemplate/index.html')
