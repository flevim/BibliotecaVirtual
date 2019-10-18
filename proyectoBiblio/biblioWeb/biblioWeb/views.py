from django.shortcuts import render
from base.models import *

def index(request):
    return render(request, 'index.html', {})

def library(request):
    def getLevels():
        return [level[1] for level in courses]


    levels = getLevels()

    context = {
        'levels':levels,
    }

    return render(request, 'library.html', context)
