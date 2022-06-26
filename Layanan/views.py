from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class MyLayanan(TemplateView):
    template_name = "templates/layanan.html"


def PageLayanan(request):
    return render('templates/layanan.html')