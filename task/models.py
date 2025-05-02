from django.db import models

# Create your models here.
class Works(models.Model):
    objects = None
    title = models.CharField(max_length= 200)
    is_complited = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    descriptoin = models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
