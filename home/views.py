from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from home.models import Contact


# Create your views here.
def home(request):
    # allposts = UserPost.objects.filter(adminStatus=True,userStatus="publish")[0:3]
    # context = {'allposts':allposts}
    # return render(request,'home/index.html',context)
    return render(request,'home/index.html')


def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        if len(name)<2 or len(email)<2 or len(phone)<5 or len(desc)<2:
            messages.error(request,"Please fill your all details correctly")
        else:
            contact = Contact(name=name,email=email,phone=phone,desc=desc) 
            contact.save()
            messages.success(request,"Your message has been successfully sent")
        return redirect('home')          
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html') 



