from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    CL = models.IntegerField(default=1)
    RH = models.IntegerField(default=1)
    TL = models.IntegerField(default=1)
    remaining_TL= models.IntegerField(default=1)
    per= models.IntegerField(default=1)
    status=models.CharField(max_length=200,default='a')
    def _str_(self):
        return self.name
