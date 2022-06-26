from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Story',
        'Heading':'Profesional Jurnal',
    }
    return render(request,'services/index_i.html',context={'context':context})