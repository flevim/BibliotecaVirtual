from django.shortcuts import render
from base.models import *

def index(request):
    return render(request, 'index.html', {})

def library(request):
    def getLevelsAndCount():
        return [(level[1], Document.objects.filter(level__exact = level[0]).count()) for level in courses]

    name_count_docs = getLevelsAndCount()

    context = {
        'name_count_docs':name_count_docs,
    }

    return render(request, 'library.html', context)

def detail_course(request, level):
    context = {
        'level':level,
    }
    return render(request, 'detail_course.html', context)
