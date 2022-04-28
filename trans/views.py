from django.shortcuts import render
from googletrans import Translator
import googletrans

# Create your views here.
def index(request):
    context = {"ndict":googletrans.LANGUAGES}
    if request.method == 'POST':
        text = request.POST.get('btext')
        bcate = request.POST.get('bcate')
        lcate = request.POST.get('lcate')
        translator = Translator()
        if text:
            inter = translator.translate(text, src=bcate, dest=lcate)
            context.update({
                'af' : inter.text,
                'text' : text,
                'bcate' : bcate,
                'lcate' : lcate
            })
    return render(request, 'trans/index.html', context)