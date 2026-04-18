from django.shortcuts import render

# Create your views here.
def index(request):
    view_user=[
        {"name":"selva","age":23},
        {"name":"sri","age":17},
        {"name":"selva","age":27},
        {"name":"selva","age":12},
    ]
    
    return render(request, "index.html",context={"users":view_user})