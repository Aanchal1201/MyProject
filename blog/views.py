from django.shortcuts import render,HttpResponse,redirect
from blog.models import UserPost
from django.contrib import messages
from datetime import datetime

# Create your views here.
def bloghome(request):
    allposts = UserPost.objects.filter(adminStatus=True,userStatus="publish")
    context = {'allposts':allposts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    if not request.user.is_authenticated:
        post = UserPost.objects.filter(slug=slug,userStatus="publish",adminStatus=True).first()
        print(post)
    else:
        post1 = UserPost.objects.filter(slug=slug,adminStatus=True,userStatus="publish")
        post2 = UserPost.objects.filter(slug=slug,authorUsername=request.user)
        post = post1.union(post2).first()

    if post is not None:
        context = {'post':post}
        return render(request,'blog/blogPost.html',context) 
    else:
        return HttpResponse("404 page not found")


def writeBlog(request):
    if not request.user.is_authenticated:
        return HttpResponse("404 page not found")
    else:
        isEmpty = False
        user_post = UserPost.objects.filter(authorUsername=request.user)
        if user_post.count() == 0:
            isEmpty = True
        return render(request,'blog/UserBlogs.html',{'userPost':user_post,'isEmpty':isEmpty})

def addBlog(request):
    if not request.user.is_authenticated:
        return HttpResponse("404 page not found")
    else: 
        return render(request,'blog/addBlog.html')
        
def handleAddBlog(request):
    if request.method == 'POST':
        title = request.POST['title']
        Label = request.POST['Label']
        category = request.POST['category']
        pubDate = request.POST['pubDate']
        content = request.POST['content']
        timeRead = request.POST['timeRead']
        image = request.FILES.get('image')
        status = request.POST['status']
        # slug = "-".join(str(title).split(" ")[0:6])
        slug = str(title).replace(" ","-")
        updatedDate = datetime.today()

        if UserPost.objects.filter(slug=slug).exists():
            messages.error(request,"Your post title already exist, Please try with another one")
            return redirect('addBlog')
        else:
            USERPOST = UserPost(authorUsername=request.user,title=title,label=Label,category=category,image=image,slug=slug,author=request.user.first_name,timeStamp=pubDate,dateUpdates=updatedDate,timeRead=timeRead,content=content,userStatus=status,adminStatus=False)
            USERPOST.save()
            messages.success(request,"User Blog is successfully created!!")
            return redirect('writeBlog')
        

def deleteUserBlog(request):
    if request.method == 'POST':
        delPost = UserPost.objects.get(slug=request.POST['del'])
        delPost.delete()
        return redirect('writeBlog')

def EditUserBlog(request):
    if request.method == 'POST':   
        editPost = UserPost.objects.get(slug=request.POST['edit'])
        context = {'post':editPost}
        return render(request,'blog/EditUserBlog.html',context)
        
def handleEditUserBlog(request):
    if request.method == 'POST':
        editPost = UserPost.objects.get(slug=request.POST['slug'])
        editPost.title = request.POST['title']
        editPost.label = request.POST['Label']
        editPost.category = request.POST['category']
        editPost.timeStamp = request.POST['pubDate']
        editPost.content = request.POST['content']
        editPost.timeRead = request.POST['timeRead']
        editPost.userStatus = request.POST['status']
        editPost.dateUpdates = datetime.today()
        Image = request.FILES.get('image')
        if Image is not None:
            editPost.image = Image

        editPost.save()
        messages.success(request,"User Blog  is updated successfully!!")
        return redirect('writeBlog')
        
def search(request):
    query = request.GET['query']
    if len(query)>80:
        allposts = UserPost.objects.none()
    else:
        allpoststitle = UserPost.objects.filter(adminStatus=True,userStatus="publish",title__icontains=query)
        allpostscontent = UserPost.objects.filter(adminStatus=True,userStatus="publish",content__icontains=query)
        allposts = allpoststitle.union(allpostscontent)
    
    if allposts.count()==0:
        messages.warning(request,"No search Results found!")
    context = {'allposts':allposts,'query':query}
    return render(request,'blog/searchBlog.html',context)