from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# from django.http import JsonResponse
import requests
import random
import json
from .forms import CommentForm,PostForm,CreateUserForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def register(request) :
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST' :
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                # Author.objects.create(user=user,name=user.username)
                messages.success(request,'Account was created for ' + str(user))
                return redirect('loginpage')
    context = {
    'form' : form
    }
    return render(request,'blog/register.html',context)


# def google(request) :
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         params = {
#             'grant_type': 'authorization_code',
#             'code': request.GET.get('code'),
#             'redirect_uri': redirect_uri,
#             'client_id': settings.GP_CLIENT_ID,
#             'client_secret': settings.GP_CLIENT_SECRET
#         }
#         url = 'https://accounts.google.com/o/oauth2/token'
#         response = requests.post(url, data=params)
#         url = 'https://www.googleapis.com/oauth2/v1/userinfo'
#         access_token = response.json().get('access_token')
#         response = requests.get(url, params={'access_token': access_token})
#         user_data = response.json()
#         email = user_data.get('email')
#         Author.objects.create(email=user,name=user.username)
#         return redirect('loginpage')
#     context = {
#     'form' : form
#     }
#     return render(request,'blog/register.html',context)


def loginpage(request) :
    if request.user.is_authenticated:
        return redirect('home')
    else :
        if request.method == 'POST' :
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username = username, password = password)
            if user is not None :
                login(request,user)
                return redirect('home')
            else :
                messages.info(request,'Username OR Password is incorrect')
    context = {
    }
    return render(request,'blog/login.html',context)

def logoutpage(request) :
    logout(request)
    context = {
    }
    return redirect('loginpage')

@login_required(login_url = 'loginpage')
def login_user(request) :
    if request.user.is_authenticated:
        name = request.user
    context = { 'name': name
    }
    return render(request,'blog/login_user.html',context)


def home(request):
    # print(request.user.author)

    try:
        if request.user.author:
            print("T")
    except:
        Author.objects.create(user=request.user,name=request.user.username)    
    # post = Post.objects.get(id = 1)
    # author = Author.objects.all()


    #single random blog
    blog_main = Post.objects.all()
    random_blog = random.choice(blog_main)

    #3 random items
    listed = list(blog_main)
    random_blogs = random.sample(listed,3)

    #latest blogs
    latest = Post.objects.all().order_by('-id')[:3]

    #all blogs
    blogs = Post.objects.all()
    paginator = Paginator(blogs,4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    context = {
    'random_blog' : random_blog,
    'random_blogs' : random_blogs,
    'latest' : latest,
    'blogs' : blogs,
    'queryset': paginated_queryset,
    'page_request_var': page_request_var,
    # 'author' : author
    }
    return render(request,'blog/home.html',context)



def blogs(request,blog_id):

    blog = Post.objects.get(pk = blog_id)
    user = request.user
    post = blog.title
    print(post)

    comments = blog.comment_set.all()
    print(comments)
    count = comments.count()

    print(request.user)

    blog_all = Post.objects.all()
    listed = list(blog_all)
    random_blogs = random.sample(listed,4)

    form = CommentForm()

    if  request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(request.POST)
            print(request.POST)

            if form.is_valid():
                print("T")
                comment = form.cleaned_data.get('comment')
                print(comment)
                form.instance.user = user
                form.instance.post = blog
                form.save()
                return redirect('blogs',blog_id)
                # comment = Comment(post = post)
                # comment.save()

    context = {
    'blog' : blog,
    'random_blogs' : random_blogs,
    'form' : form,
    'comments' : comments,
    'count' : count

    }
    return render(request,'blog/blog.html',context)


def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        blogs = Post.objects.filter(title__startswith = search)
        print(blogs)

    context = {
    'blogs' : blogs,
    'search' : search
    }
    return render(request,'blog/search.html',context)


@login_required(login_url = 'loginpage')
def comment_delete(request,blog_id,comment_id):
        blog = Post.objects.get(pk = blog_id)
        print(blog)

        comments = Comment.objects.filter(pk = comment_id).delete()
        return redirect('blogs',blog_id)


@login_required(login_url = 'loginpage')
def blog_create(request):

    title = 'create'
    form = PostForm()
    author = Author.objects.get(user = request.user)
    print(request.user)

    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        print(request.POST)

        if form.is_valid():
            print("T")
            # comment = form.cleaned_data.get('comment')
            form.instance.author = author
            # form.instance.post = blog
            form.save()
            return redirect('home')

    context = {
    'form' : form,
    'title' : title,
    }
    return render(request,'blog/blog_create.html',context)

@login_required(login_url = 'loginpage')
def blog_update(request,blog_id):

    title = 'update'
    post = Post.objects.get(pk = blog_id)
    print(post)
    form = PostForm(instance = post)


    author = Author.objects.get(user = request.user)
    print(request.user)

    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,instance = post)
        if form.is_valid():
            print("T")
            # comment = form.cleaned_data.get('comment')
            form.instance.author = author
            # form.instance.post = blog
            form.save()
            return redirect('home')

    context = {
    'form' : form,
    'title' : title,
    }
    return render(request,'blog/blog_create.html',context)

@login_required(login_url = 'loginpage')
def blog_delete(request,blog_id):

    post = Post.objects.get(pk = blog_id)
    post.delete()
    return redirect('home')

    context = {
    'form' : form

    }
    return render(request,'blog/blog_create.html',context)

def author_blogs(request,name):
    print("name is " + str(name))
    author = Author.objects.get(name = name)
    print(author.id)


    blogs = Post.objects.filter(author = author.id)
    print(blogs)

    context = {
    'blogs' : blogs
    }
    return render(request,'blog/author.html',context)


# def update_user_social_data(strategy, *args, **kwargs):
#     response = kwargs['response']
#     backend = kwargs['backend']
#     user = kwargs['user']

#     if response['picture']:
#         url = response['picture']
#         userProfile_obj = Author()
#         userProfile_obj.user = user
#         userProfile_obj.picture = url
#         userProfile_obj.save()
