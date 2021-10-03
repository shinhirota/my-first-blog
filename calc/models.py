from django.db import models


class Param(models.Model):
    arg1 = models.CharField(max_length=10)
    arg2 = models.CharField(max_length=10)
