from django import forms
from django.core.exceptions import ValidationError

from photos.models import Photo
from photos.settings import BADWORDS


class PhotoForm(forms.ModelForm):
    """
    Formulario para el modelo Photo
    """

    class Meta:
        model = Photo
        exclude = ['owner', ]

    # def clean(self):
    #     """
    #     Valida si en la descripción se ponen las palabras restringidos
    #     :return: direccionario con los atributos
    #     """
    #     cleaned_data = super(PhotoForm, self).clean()
    #     description = cleaned_data.get('description', '')
    #
    #     for badword in BADWORDS:
    #         if badword.lower() in description.lower():
    #             raise ValidationError(
    #                 'La palabra {0} no esta permitida'.format(badword))  # poner u delante en python 2 'unidcode'
    #
    #     # devuelve los datos normalizados
    #     return cleaned_data
