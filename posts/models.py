from django.db import models
from django.conf import settings


class Paradigm(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
        
class Language(models.Model):
    name = models.CharField(max_length=120)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Programmer(models.Model):
     name = models.CharField(max_length=120)
     languages = models.ManyToManyField(Language)

     def __str__(self):
        return self.name