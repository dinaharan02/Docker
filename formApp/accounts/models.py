from django.db import models
from django.contrib.auth.models import User, Group


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')
    mobile_number = models.IntegerField()

    class Meta:
        db_table = 'User Profile'
        verbose_name_plural = 'User Profile'

    def __str__(self):
        return str(self.user)
