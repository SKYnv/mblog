from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from .forms import PostForm, LoginForm, RegisterForm
from .models import UserPost
from django.utils import timezone


def getpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('body_text')
            user = request.user
            if user is None:
                return HttpResponseRedirect('/login')

            f = UserPost()
            f.post_text = text
            f.post_user = user
            f.post_date = timezone.now()
            f.save()
            return HttpResponseRedirect('/')


def userprofile(request, user_name):
    try:
        user_name = user_name.replace('/profile', '')
        user = User.objects.get(username=user_name)
    except:
        pass
    return render(request, 'mblog/userprofile.html', {'user': user, })


def search(request, user_name):
    user = request.user
    post_autor = User.objects.get(username=user_name)
    user_posts = UserPost.objects.filter(post_user=post_autor)
    user_posts = user_posts.order_by('-post_date')[:10]
    return render(request, 'mblog/userposts.html', {'user_posts': user_posts, 'user': user, 'autor': post_autor})


def index(request):
    user = request.user
    last_post = UserPost.objects.order_by('-post_date')[:10]

    if user.is_authenticated:
        postform = PostForm()
        context_dict = {'user': user, 'form': postform, 'last_post': last_post}
    else:
        lform = LoginForm()
        context_dict = {'user': user, 'last_post': last_post, 'lform': lform}
    if request.method == 'POST':
        lform = LoginForm(request.POST)
        if lform.is_valid():
            name = lform.cleaned_data['user_login']
            pwd = lform.cleaned_data['user_password']
            user_login(request, name, pwd)
            context_dict = {'user': user, 'last_post': last_post, 'lform': lform}
            return HttpResponseRedirect('/')
        getpost(request)
    return render(request, 'mblog/index.html', context_dict)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_login(request, name, pwd):
    user = authenticate(username=name, password=pwd)
    if user is not AnonymousUser:
        login(request, user)

    if user is not None:
        # the password verified for the user
        if user.is_active:
            # print("User is valid, active and authenticated")
            pass
        else:
            # print("The password is valid, but the account has been disabled!")
            pass
    else:
        # the authentication system was unable to verify the username and password
        # print("The username and password were incorrect.")
        pass


def register_user(request):
    rf = RegisterForm()
    if request.method == 'POST':
        rf = RegisterForm(request.POST)
        if rf.is_valid():
            email = rf.cleaned_data.get('user_email')
            pwd = rf.cleaned_data.get('user_password')
            fname = rf.cleaned_data.get('user_firstname')
            lname = rf.cleaned_data.get('user_lastname')
            newuser = User()
            newuser.username = email
            newuser.email = email
            newuser.password = pwd
            newuser.set_password(pwd)  # иначе аброкадабра в базе
            newuser.first_name = fname
            newuser.last_name = lname
            newuser.save()
            user_login(request, email, pwd)
            return HttpResponseRedirect('/')
        else:
            rf = RegisterForm()

    context_dict = {'regform': rf, }
    return render(request, 'mblog/register.html', context_dict)
