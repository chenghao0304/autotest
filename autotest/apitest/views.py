from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    # return HttpResponse("Hello Django!")
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        # authenticate()函数认证给出的用户名和密码。它接受两个参数：username和password，并且会在用户名密码正确的情况下返回一个user独享，否则返回None
        if user is not None:
            auth.login(request, user)  # login
            response = HttpResponseRedirect('/home/')
            request.session['user'] = username  # 将session信息记录到浏览器
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')
