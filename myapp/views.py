from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def movie(request):
    return HttpResponse("Hello Michael")

def template_view(request):
    data={'movies':[
        {
            'id': 1,
            'title': 'magic',
            'year': '2004'
        },
          {
            'id': 1,
            'title': 'horror',
            'year': '2005'
        },
          {
            'id': 1,
            'title': 'fantasy',
            'year': '2003'
        }
    ]}

    return render(request,'movie.html', data)


