from django.db import models

class FavouriteDog(models.Model):
  link = models.CharField(max_length=200)

  def __str__(self):
    return f'{self.link}'