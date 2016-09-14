from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django import forms
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from django.contrib.auth import authenticate
from .forms import PostForm, LoginForm
from .models import UserPost
from django.utils import timezone
import datetime


# Create your views here.


def getpost(request):
    if request.method == 'POST':
        text = request.POST['body_text']
        user = request.user
        if user is None:
            return HttpResponseRedirect('/login')

        # todo использовать контекст для коммита
        f = UserPost()
        f.post_text = text
        f.post_user = user
        f.post_date = timezone.now()
        f.save()
        return HttpResponseRedirect('/test')


def search(request, user_name):
    user = request.user
    post_autor = User.objects.get(username=user_name)
    template = loader.get_template('mblog/userposts.html')
    user_posts = UserPost.objects.filter(post_user=post_autor)[:10]
    context = RequestContext(request, {'user_posts': user_posts, 'user': user})
    return HttpResponse(template.render(context))


def index(request):
    template = loader.get_template('mblog/index.html')
    user = request.user
    last_post = UserPost.objects.order_by('-post_date')[:10]

    if user.is_authenticated:
        # todo проверка формы
        # todo csrf token
        # todo переделать на ModelForm
        f = PostForm()
        context_dict = {'user': user, 'form': f, 'last_post': last_post, }
    else:
        tt = LoginForm()
        context_dict = {'user': user, 'loginform': tt, 'last_post': last_post, }

    getpost(request)
    context = RequestContext(request, context_dict)

    return HttpResponse(template.render(context))


def exit(request):
    logout(request)
    return HttpResponseRedirect('/')


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "mblog/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "mblog/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
