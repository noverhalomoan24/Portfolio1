from django.shortcuts import render


def index(request):
    context = {
        'title':'Home',
        'heading':'selamat Datang',
    }
    return render(request,'index.html',context={'context':context})