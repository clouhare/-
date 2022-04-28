from django.shortcuts import redirect, render
from .models import Book
# Create your views here.
def index(request):
    b = request.user.book_set.all()
    context = {
        "bset" : b
    }
    return render(request, 'book/index.html', context)

def create(request):

    if request.method == 'POST':
        sn = request.POST.get('sname')
        su = request.POST.get("surl")
        sc = request.POST.get('scom')
        im = bool(request.POST.get('impo'))
        Book(user=request.user, sitename=sn, site_url=su, comment=sc, impo=im).save()
        return redirect('book:index')
    return render(request, 'book/create.html')