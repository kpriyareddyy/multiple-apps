from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':30,'b':20}
    return render(request,'a2_first.html',d)

def a2_second(request):
    d={'a':30,'b':60,'c':100}
    return render(request,'a2_second.html',d)