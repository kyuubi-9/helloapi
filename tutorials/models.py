from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    
