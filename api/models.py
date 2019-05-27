from django.db import models

# Create your models here.

class Api(models.Model):
    first_name = models.CharField(max_length=10,  default='')
    last_name = models.CharField(max_length=10,  default='')
    company_name = models.CharField(max_length=50,  default='')
    email = models.CharField(max_length=50,  default='')
    city = models.CharField(max_length=15,  default='')
    state = models.CharField(max_length=15,  default='')
    web = models.CharField(max_length=50,  default='')
    age = models.IntegerField(blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.first_name+self.first_name