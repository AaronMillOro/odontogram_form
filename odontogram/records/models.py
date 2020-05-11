from django.db import models
from django.utils.timezone import now


class Mouth(models.Model):
    """Odontogram"""
    date = models.DateTimeField(default=now, editable=False)
    t_11 = models.CharField(max_length=70, default='sano')
    t_12 = models.CharField(max_length=70, default='sano')
    t_13 = models.CharField(max_length=70, default='sano')
    #t_14 = models.ManyToManyField('Proceeding', blank=True)
    #t_15 = models.ManyToManyField('Proceeding', blank=True)
    #t_16 = models.ManyToManyField('Proceeding', blank=True)
    #t_17 = models.ManyToManyField('Proceeding', blank=True)
    #t_18 = models.ManyToManyField('Proceeding', blank=True)
