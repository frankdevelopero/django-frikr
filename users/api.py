from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from users.permissions import UserPermission
from users.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    permission_classes = (UserPermission,)

    def list(self, request):
        paginator = PageNumberPagination()
        users = User.objects.all()

        # paginar el queryset
        paginator.paginate_queryset(users, request)
        serializer = UserSerializer(users, many=True)  # Serializa estos objetos y guarda en atributo data

        # devolver la respuesta paginada
        return paginator.get_paginated_response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # devuelve el usuario creado
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        user = get_object_or_404(User, pk=pk)  # si exite devuelve si no lanza una excepcion
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        json = {
            "mensaje": "Usuario borrado con éxito"
        }
        return Response(json, status=status.HTTP_204_NO_CONTENT)
