from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.db.models import Q
from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC


class PhotosQuerySet(object):
    @staticmethod
    def get_photos_queryset(request):
        if not request.user.is_authenticated:
            photos = Photo.objects.filter(visivility=PUBLIC)
        elif request.user.is_superuser:
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(Q(owner=request.user) | Q(visivility=PUBLIC))

        return photos


class HomeView(View):

    def get(self, request):
        photos = Photo.objects.filter(visivility='PUB').order_by('-create_at')
        context = {
            'photos_list': photos[:9]
        }
        return render(request, 'photos/home.html', context)


class PhotoDetailView(View, PhotosQuerySet):

    def get(self, request, pk):
        # pk es el identificador para el detalle de una foto

        possible_photos = self.get_photos_queryset(request).filter(pk=pk).select_related('owner')
        # cuando la relacion es inversa usar prefetch_related

        photo = possible_photos[0] if len(possible_photos) == 1 else None

        if photo is not None:
            context = {
                'photo': photo
            }
            return render(request, 'photos/detail.html', context)

        else:
            return HttpResponseNotFound('No exite la foto')


# class OnlyAutenticateView(View):
#     def get(self, request):
#         if request.user.is_authenticated():
#             return super(OnlyAutenticateView, self).get(request)
#         else:
#             pass


class CreateView(View):

    @method_decorator(login_required())
    def get(self, request):
        # Muestra un formulario para crear una foto

        form = PhotoForm()
        context = {
            'form': form,
            'succes_message': ''
        }

        return render(request, 'photos/new_photo.html', context)

    @method_decorator(login_required())
    def post(self, request):
        # Crea una foto en base a la informació POST

        success_message = ''
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user  # asigna como propietario
        form = PhotoForm(request.POST, instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save()  # Guarda el objeto y devuelve
            form = PhotoForm()
            success_message = '¡Guardado con éxito!'
            success_message += '<a ref="{0}">'.format(reverse('photos_detail', args=[new_photo.pk]))
            success_message += 'Ver foto'
            success_message += '</a>'
        context = {
            'form': form,
            'succes_message': success_message
        }

        return render(request, 'photos/new_photo.html', context)


class PhotoListView(View, PhotosQuerySet):

    def get(self, request):
        """
        Devuelve
        -Las fotos publicas si el usuario no esta autentificada
        -Las fotos del usuario autentificado
        -Si el usuario es SuperoAdmin todas las fotos
        :param request:
        :return:
        """

        context = {
            'photos': self.get_photos_queryset(request)
        }

        return render(request, 'photos/photos_list.html', context)

        """
        Devuelve:
        Todas las fotos cuyo autor tiene un nombre en específico
        Queries avanzadas
        """
        #  photos = Photo.objects.filter(owner__fisrt_name = 'Alberto')


class UserPhotosView(ListView):
    model = Photo
    template_name = 'photos/user_photos.html'

    def get_queryset(self):
        queryset = super(UserPhotosView, self).get_queryset()
        return queryset.filter(owner=self.request.user)
