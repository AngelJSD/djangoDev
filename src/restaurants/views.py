import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home (request):
    
    var_number = random.randint(0, 1000000)
    #return HttpResponse("hello")
    return render(request, "base.html", {"number" : var_number}) #response