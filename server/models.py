from django.db import models

class User(models.Model):
   name = models.CharField(max_length=100)
   username = models.CharField(max_length=100)
   email = models.EmailField(max_length=100)

   def _str_(self):
       return self.name