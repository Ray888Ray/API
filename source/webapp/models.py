from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='name')
    accesses = models.ManyToManyField(User, related_name='accessed_products')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='name')
    video_link = models.URLField()
    duration_seconds = models.PositiveIntegerField(null=False, blank=False, verbose_name='duration')
    viewed_status = models.BooleanField(default=False)
    viewed_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
