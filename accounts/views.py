from django.http import HttpResponse
from django.shortcuts import redirect, render
from accounts.models import User
from accounts.forms import UserForm
from django.contrib import messages
from vendor.forms import VendorForm

# Create your views here.
def registerUser(request):
    if request.method =="POST":
        # print(request.POST)
        form= UserForm(request.POST)
        if form.is_valid():
           #Create the user using the form
        #    password = form.cleaned_data['password']
           
        #    user = form.save(commit=False)
           
        #    user.set_password(password)
           
        #    user.role=User.CUSTOMER
        #    user.save()
        
        
        # Create user using create user method

            first_name = form.cleaned_data['first_name']
            last_name =form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
            user.role =User.CUSTOMER
            user.save()
            # print('User is created')
            messages.success(request,"your account has been registered sucessfully")

           
            return redirect('registerUser')
        else:
           print('Invalid form')
           print(form.errors)
    else:

     form = UserForm()
    context={
        'form':form,

    }

    return render(request,'accounts/registeruser.html',context)




def registerVendor (request):
   
   form = UserForm()
   v_form = VendorForm()
   context = {
      'form':form,
      'v_form':v_form



   }
   
   
   return render(request,'accounts/registerVendor.html',context)