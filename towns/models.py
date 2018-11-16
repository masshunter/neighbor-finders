from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class Neighbors(models.Model):
#     from_state = models.CharField(max_length=20)
#     from_district = models.CharField(max_length=20)
#     from_town = models.CharField(max_length=20)
#     deg_range = models.CharField(max_length=10)
#     to_state = models.CharField(max_length=20)
#     to_district = models.CharField(max_length=20)
#     to_town = models.CharField(max_length=20)
#
#     def publish(self):
#         self.save()
#
#     def __str__(self):
#         return self.from_state + "-" + self.from_district + "-" + self.from_town + ": "
#         + self.deg_range + "/" + self.to_state + "-" + self.to_district + "-" + self.town
