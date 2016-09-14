from django.db import models
from django.contrib.auth.models import User


class UserPost(models.Model):
    post_text = models.TextField(max_length=140)
    post_user = models.ForeignKey(User, null=True, related_name='+')
    post_date = models.DateTimeField()

    def __str__(self):
        return self.post_text
