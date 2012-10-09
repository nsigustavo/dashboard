from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    url_git = models.CharField(max_length=256, null=False, blank=False)
    date_created = models.DateField(auto_now_add=True, editable=False)
