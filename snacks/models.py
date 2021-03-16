from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Snack(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(default='')
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__():
        return f'Found {self.name} on {self.purchaser}\'s list becuase {self.description}'