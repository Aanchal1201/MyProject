from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create Registraton View 
def signup(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else:
        if request.method == 'POST':
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            cpass = request.POST['cpass']

            if password != cpass:
                messages.error(request,"Your password not match with confirm password")
                return redirect('signup')
            elif User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.error(request,"Your username/email already exists, Try to Login")
                return redirect('signup')

            myuser = User.objects.create_user(username,email,password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request,"You are registered in our website successfully")
            return redirect('userLogin')
        return render(request,'account/signup.html') 

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else:
        if request.method == 'POST':
            email = request.POST['username']
            password = request.POST['password']
            
            # if user enter email
            if email.find("@") == -1:
                username = email
            else:
                try:
                    username = User.objects.get(email=email.lower()).username
                except User.DoesNotExist:
                    messages.error(request,"Invalid Credentials, Please try again")
                    return redirect('home')

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Successfully logged In")
                return redirect('home')
            else:
                messages.error(request,"Invalid Credentials, Please try again")
                return redirect('home')
        return render(request,'account/login.html') 

def userLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('home')

def changePass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            oldPass = request.POST['oldPass']
            newPass = request.POST['newPass']
            cnewpass = request.POST['cnewpass']
            user = authenticate(username=request.user,password=oldPass)  
            if newPass != cnewpass:
                messages.error(request,"Your password not match with confirm password")  
            elif user is not None:
                user.set_password(newPass)
                user.save()
                messages.success(request,"Password change successfully")
                return redirect('home')
            else:
                messages.error(request,"Your old Password is not correct")
            return redirect('changePass')
        return render(request,'account/changePassword.html')
    else:
        return redirect('home')

