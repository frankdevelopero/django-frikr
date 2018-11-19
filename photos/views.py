from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from photos.models import Photo


# Create your views here.
def home(request):
    photos = Photo.objects.filter(visivility='PUB').order_by('-create_at')
    context = {
        'photos_list': photos[:9]
    }
    return render(request, 'photos/home.html', context)


def detail(request, pk):
    # pk es el identificador para el detalle de una foto

    possible_photos = Photo.objects.filter(pk=pk)

    photo = possible_photos[0] if len(possible_photos) == 1 else None

    if photo is not None:
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)

    else:
        return HttpResponseNotFound('No exite la foto')

