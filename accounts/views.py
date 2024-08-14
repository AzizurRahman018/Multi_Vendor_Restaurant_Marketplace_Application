from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserForm
# Create your views here.
def registerUser(request):
    if request.method =="POST":
        print(request.POST)
        form= UserForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('registerUser')
    else:

     form = UserForm()
    context={
        'form':form,

    }

    return render(request,'accounts/registeruser.html',context)