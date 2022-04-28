from django.shortcuts import render, redirect
from .models import Board, Reply
from django.utils import timezone
from acc.models import User
# Create your views here.
from django.core.paginator import Paginator
def index(request):
    pg = request.GET.get('page', 1)
    cate = request.GET.get('cate', '')
    kw = request.GET.get('kw', '')
    if kw:
        if cate == 'sub':
            b = Board.objects.filter(subject__startswith=kw)
        elif cate == 'wri':
            try:
                u = User.objects.get(username = kw)
                b = Board.objects.filter(writer=u)
            except:
                b = Board.objects.none()
        elif cate == 'con':
            b = Board.objects.filter(content__contains=kw)
    else:
        b = Board.objects.all()
    b = b.order_by('-pubdate')
    pag = Paginator(b, 10)
    obj = pag.get_page(pg)
    context = {
        "bset" : obj,
        'cate' : cate,
        'kw' : kw
    }
    return render(request, 'board/index.html', context)

def detail(request, bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all()
    context = {
        "b" : b,
        "rset" : r
    }
    return render(request, 'board/detail.html', context)



def delete(request, bpk):
    b = Board.objects.get(id=bpk)
    if request.user == b.writer:
        b.delete()
    else:
        pass
    return redirect('board:index')

def create(request):
    if request.method == "POST":
        s = request.POST.get('sub')
        c = request.POST.get('con')
        if s and c:
            Board(subject = s, writer = request.user, content = c, pubdate = timezone.now()).save()
            return redirect('board:index')
    return render(request, 'board/create.html')

def update(request, bpk):
    b = Board.objects.get(id=bpk)
    context = {
        "b" : b
    }

    if request.user != b.writer:
        return redirect('board:index')
    
    if request.method == "POST":
        s = request.POST.get('sub')
        c = request.POST.get('con')
        b.subject = s
        b.content = c
        b.save()
        return redirect('board:detail', bpk)
    return render(request, 'board/update.html', context)

def creply(request, bpk):
    c = request.POST.get("com")
    b = Board.objects.get(id=bpk)
    Reply(b = b, replyer = request.user, comment = c, pubdate = timezone.now()).save()
    return redirect('board:detail', bpk)

def dreply(request, bpk, rpk):
    r = Reply.objects.get(id=rpk)
    if r.replyer == request.user:
        r.delete()
        return redirect('board:detail', bpk)

def likey(request, bpk):
    b = Board.objects.get(id = bpk)
    b.likey.add(request.user)
    return redirect('board:detail', bpk)

def unlikey(request, bpk):
    b = Board.objects.get(id = bpk)
    b.likey.remove(request.user)
    return redirect('board:detail', bpk)