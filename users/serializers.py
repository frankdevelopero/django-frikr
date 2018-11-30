from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()  # Solo  campo de lectura
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Crea una instancia de User a partir de los datos de Validate Data
        que contienes valores deserializados
        :param validated_data: Diccionario con datos de Usuario
        :return: objeto User
        """
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza una instancia a partir de los datos
        :param instance:
        :param validated_data:
        :return: objeto actualizado
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        """
        Valida si existe un usuario con el mismo usuario
        :param data:
        :return: Data
        """
        users = User.objects.filter(username=data)
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError("Este usuario ya esta registrado")

        elif self.instance and self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError("Este usuario ya esta registrado")

        else:
            return data
