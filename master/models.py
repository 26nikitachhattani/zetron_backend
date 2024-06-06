from django.db import models

# Create your models here.
class category(models.Model):
    name = models.TextField(max_length=200,default=None)
    description = models.TextField(default=None)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created',]
