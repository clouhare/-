from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User
# Create your views here.
def index(request):
    return render(request, "acc/index.html")

def login_user(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        pw = request.POST.get("upass")
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect("acc:index")
        else:
            pass
    return render(request, "acc/login.html")

def logout_user(request):
    logout(request)
    return redirect('acc:index')

def profile(request):
    return render(request, 'acc/profile.html')

def signup(request):
    if request.method == "POST":
        un= request.POST.get('uname')
        up = request.POST.get('upass')
        ua = request.POST.get('uage')
        uc = request.POST.get('ucom')
        ui = request.FILES.get('upic')
        try:
            User.objects.create_user(username = un, password = up, age = ua, comment = uc, pic = ui)
        except:
            pass
        return redirect('acc:index')
    return render(request, 'acc/signup.html')

def update(request):
    if request.method == "POST":
        u = request.user
        un = request.POST.get('uname')
        up = request.POST.get('upass')
        ua = request.POST.get('uage')
        uc = request.POST.get('ucom')
        ui = request.FILES.get('upic')
        u.username = un
        u.age = ua
        u.comment = uc
        if ui:
            request.user.pic.delete()
            u.pic = ui
        if up:
            u.set_password(up)
            login(request, u)
        u.save()
        return redirect('acc:profile')
    return render(request, 'acc/update.html')

def delete(request):
    ck = request.POST.get('ckp')
    if check_password(ck, request.user.password):
        request.user.pic.delete()
        request.user.delete()
        return redirect("acc:index")
    else:
        pass
    return redirect("acc:profile")