from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from photos.forms import PhotoForm
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

    possible_photos = Photo.objects.filter(pk=pk).select_related('owner') # cuando la relacion es inversa usar prefetch_related

    photo = possible_photos[0] if len(possible_photos) == 1 else None

    if photo is not None:
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)

    else:
        return HttpResponseNotFound('No exite la foto')

@login_required()
def create(request):
    # Muestra un formulario para crear una foto y lo crea si es POST

    success_message = ''

    if request.method == 'POST':
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user  # asigna como propietario
        form = PhotoForm(request.POST, instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save()  # Guarda el objeto y devuelve
            form = PhotoForm()
            success_message = '¡Guardado con éxito!'
            success_message += '<a ref="{0}">'. format(reverse('photos_detail', args=[new_photo.pk]))
            success_message += 'Ver foto'
            success_message += '</a>'
    else:
        form = PhotoForm()
    context = {
        'form': form,
        'succes_message': success_message
    }

    return render(request, 'photos/new_photo.html', context)
