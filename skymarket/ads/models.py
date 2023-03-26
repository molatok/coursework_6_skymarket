from django.conf import settings
from django.db import models
from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=25)
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='django_media/', default=None)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=250)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text