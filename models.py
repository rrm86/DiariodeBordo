from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Record(models.Model):
    RECORD_TYPE = (
        ('P','Personal'),
        ('S', 'Study'),
        )
    CATEGORY_CHOICES =(
        ('django','Django'),
        ('redes1','Redes1'),
        ('prog3','Prog3'),
        ('arqs','Arquitetura de Sistemas'),
        ('pensamentos','Pensamentos'),
        )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    trecord = models.CharField(max_length=100, choices=RECORD_TYPE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def  __str__(self):
        return self.title

