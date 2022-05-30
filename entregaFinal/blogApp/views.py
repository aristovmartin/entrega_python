from django.shortcuts import render
from .models import *
from .forms import *
from datetime import *
from django.contrib.auth.decorators import *


# Create your views here.

def main(request):
    blogs = Blog.objects.all()
    today = datetime.now().date()
    return render(request,'main.html',{"blogs":blogs,"fecha_hoy":today})
