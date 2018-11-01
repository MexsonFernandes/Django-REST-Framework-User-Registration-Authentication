from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=50)

    def __str__(self):
        return "{} -{}".format(self.username, self.email)
