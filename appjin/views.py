from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={
        'name':"sambit",'age':25,'place':"berhampur"
    }
    return render(request,'jinja_print.html',context=d)
