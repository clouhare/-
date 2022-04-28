from django.shortcuts import render
import pdfplumber
# Create your views here.

def index(request):
    context = {}
    if request.method == 'POST':
        p = request.FILES.get('pdf')
        if p:
            pdf = pdfplumber.open(p)
            pnum = len(pdf.pages)
            st = ''
            for i in range(pnum):
                page = pdf.pages[i]
                st += "="*30 + '\n'
                st += f"{i+1} PAGE TEXT" + "\n"
                st += "="*30 + "\n"
                st +=page.extract_text()
                st += '\n'
            context["st"] = st
        else:
            st = '변환 할 파일을 선택해주세요'
            context["st"] = st
    return render(request, 'pdfread/index.html', context)