from rest_framework.exceptions import ValidationError

from photos.settings import BADWORDS


def badwords_detector(value):
    """
    Valida si en value han puesto las palabras restringidos
    :return: Boolean
    """

    for badword in BADWORDS:
        if badword.lower() in value.lower():
            raise ValidationError(
                'La palabra {0} no esta permitida'.format(badword))  # poner u delante en python 2 'unidcode'

    # devuelve los datos normalizados
    return True
