from django.shortcuts import render
from base.models import *

def index(request):
    news = News.objects.filter(
        is_public = True,
        relevant = True,

    ).order_by('publication_date')[:3]

    context = {
        'news':news,
    }
    return render(request, 'index.html', context)


def library(request):
    def getLevelsAndCount():
        return [(level[1], Document.objects.filter(level__exact = level[0]).count()) for level in courses]

    name_count_docs = getLevelsAndCount()

    context = {
        'name_count_docs':name_count_docs,
    }

    return render(request, 'library.html', context)


def detail_course(request, level):

    def getLevels():
        return [level[1] for level in courses]

    def getActualLevel(level):
        for l in courses:
            if l[1] == level: return l[0]

    try:
        paute_docs = Document.objects.filter(
            level__exact = getActualLevel(level),
            is_guide_document = True,
        )

        educative_docs = Document.objects.filter(
            level__exact = getActualLevel(level),
            is_guide_document = False,
        )

    except:
        docs = None

    context = {
        'levels': getLevels(),
        'actual_level':level,
        'paute_docs': paute_docs,
        'educative_docs': educative_docs,
    }
    return render(request, 'detail_course.html', context)


def detail_document(request, level, doc):
    info_doc = Document.objects.filter(title__exact=doc)
    print(info_doc)
    print(info_doc.description)
    context = {
        'actual_doc':doc,
        'doc_title':doc.title,
        
        'actual_level':level,
    }
    return render(request, 'detail_document.html', context)
