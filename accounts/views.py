from django.http import HttpResponse
from django.shortcuts import redirect, render
from accounts.models import User ,UserProfile
from accounts.forms import UserForm 
from django.contrib import messages,auth
from vendor.forms import VendorForm

# Create your views here.
def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('dashboard')
    elif request.method =="POST":
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
   if request.user.is_authenticated:
        messages.warning(request, "You are already logged in! ")
        return redirect('dashboard')
   elif request.method =="POST":
       form = UserForm(request.POST)
       v_form = VendorForm(request.POST ,request.FILES)
       if form.is_valid() and v_form.is_valid():
           first_name = form.cleaned_data['first_name']
           last_name =form.cleaned_data['last_name']
           username = form.cleaned_data['username']
           email = form.cleaned_data['email']
           password = form.cleaned_data['password']
           user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
           user.role= User.VENDOR
           user.save()
           vendor = v_form.save(commit=False)
           vendor.user = user
           user_profile = UserProfile.objects.get(user=user)
           vendor.user_profile = user_profile
           vendor.save()
           
           messages.success(request,"your account has been registered sucessfully")

    
           return redirect('registerVendor')
       
       else:
           print("Invalid form")
           print(form.errors)
   else :
      

        form = UserForm()
        v_form = VendorForm()
   context = {
      'form':form,
      'v_form':v_form



   }
   
   
   return render(request,'accounts/registerVendor.html',context)

def login(request):
    if request.user.is_authenticated:
        messages.warning( request, "You are already logged in! ")
        return redirect('dashboard')
    elif request.method == "POST":
        email= request.POST["Email"]
        Password = request.POST["Password"]
    
        user=auth.authenticate(email=email,password=Password)
        if user is not None :
            auth.login(request,user)
            messages.success(request,"You are login .")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalide login")
            return redirect('login')
    return render(request,"accounts/login.html")

def logout(request):
    auth.logout(request)
    messages.info(request,"You are logout")

    return redirect ("login")

def dashboard(request):


    return render(request,"accounts/dashboard.html")