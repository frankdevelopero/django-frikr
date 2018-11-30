from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.views import PhotosQuerySet


class PhotoViewSet(PhotosQuerySet, ModelViewSet):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = (SearchFilter, OrderingFilter,)
    ordering_fields = ('name', 'owner',)
    search_fields = ('name', 'owner__first_name')

    # Verificando las autentificaciones
    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    # devolver serializer dependiendo de la peticion
    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        else:
            return PhotoSerializer

    # Antes de guardar asignamos el owner
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
