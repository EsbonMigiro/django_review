from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, Http404
from .models import movies_model

# Create your views here.

def movie(request):
    return HttpResponse("Hello Michael")

def template_view(request):
    data = movies_model.objects.all()
    return render(request,'movie.html', {'movies': data})

def details(request, id):
    data = movies_model.objects.get(pk=id)
    return render(request, 'detail.html', {'movie': data})

def add_view(request):
    title=request.POST.get('title')
    year=request.POST.get('year')

    if title and year:
        movie = movies_model(title=title, year=year)
        movie.save()

        return HttpResponseRedirect('/temp')

    return render(request, 'add.html')

def delete(request, id):
    try:

       movie=movies_model.objects.get(pk=id)
    except:
        raise Http404('NO page')
    movie.delete()
    return HttpResponseRedirect('/temp')

