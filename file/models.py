from django.db import models
from django.contrib.auth.models import User
import os


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=200)
    filetype = models.CharField(max_length=10, default='Undefined')
    file = models.FileField()
    dateUploaded = models.DateTimeField()

    def __str__(self):
        return self.filename

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension[1:]
