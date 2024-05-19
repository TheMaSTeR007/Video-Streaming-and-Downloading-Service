from django.shortcuts import render, HttpResponse

from movie.models import FilmDetails, Bollywood, Hollywood, Webseries

from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    vari = FilmDetails.objects.all()
    # vari = FilmDetails.objects.all()[:4]
    # var3 = FilmDetails.objects.all()[13:16]
    var2 = FilmDetails.objects.all()[4:12]
    var4 = FilmDetails.objects.all()[19:27]
    context = {
        'vari': vari, 'var2': var2,
        # 'var3': var3,
        'var4': var4
    }
    return render(request, 'index.html', context)


def videoView(request, video_id):
    varv = get_object_or_404(FilmDetails, pk=video_id)
    context = {
        'varv': varv,
    }
    return render(request, 'video_view.html', context)


def nav(request):
    return render(request, 'nav.html')


def movies(request):
    var3 = FilmDetails.objects.all()[0:19]
    context = {
        'var3': var3
    }
    return render(request, 'movies.html', context)


def webseries(request):
    var4 = FilmDetails.objects.all()[19:40]
    context = {
        'var4': var4
    }
    return render(request, 'webseries.html', context)

def bollywood(request):
    varB = FilmDetails.objects.all()[10:25]

    context = {
        'varB': varB
    }
    return render(request, 'bollywood.html', context)

def hollywood(request):
    varH = FilmDetails.objects.all()[25:40]

    context = {
        'varH': varH
    }
    return render(request, 'hollywood.html', context)


def search(request):
    if 'search' in request.POST:
        filmName = request.POST['search']
        # Filter blog details by filmName if search query is present
        varS = FilmDetails.objects.filter(title__icontains=filmName)[::-1]
        var2 = FilmDetails.objects.all()[4:12]
        var4 = FilmDetails.objects.all()[19:27]
        context = {
            'var2': var2, 
            # 'var3': var3,
            'var4': var4, 'varS': varS
        }

        return render(request, 'index.html', context)
    else:
        return HttpResponse('Film not available now..,try searching other films...')
