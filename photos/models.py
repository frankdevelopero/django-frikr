# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from photos.settings import LICENSES


PUBLIC = 'PUB'
PRIVATE = 'PRI'

VISIVILITY = (
    (PUBLIC, 'Públic'),
    (PRIVATE, 'Private')
)


class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, default="", null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    licence = models.CharField(max_length=3, choices=LICENSES)
    visivility = models.CharField(max_length=3, choices=VISIVILITY, default=PUBLIC)

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ["-create_at"]
