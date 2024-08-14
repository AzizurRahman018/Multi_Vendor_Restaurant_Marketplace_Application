from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm
# Create your views here.
def registerUser(request):
    form = UserForm()
    context={
        'form':form,



    }

    return render(request,'accounts/registeruser.html',context)