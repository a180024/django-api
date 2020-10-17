from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage
import os

User = get_user_model()

def upload_file(instance, filename):
    return f"{instance.user}/{filename}"

class FileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        return name

    def _save(self, name, content):
        if self.exists(name):
            return name
        return super(FileSystemStorage, self)._save(name, content)

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_file, storage=FileSystemStorage(), validators=[FileExtensionValidator(allowed_extensions=['txt'])])
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    sensitivity_score = models.IntegerField(null=True)
    flag = models.BooleanField(default=False)

    def __repr__(self):
        return f"{self.file.name} uploaded by {self.user}"

    def __str__(self):
        return f"{self.file.name}"

    def reset_flag_and_sensitivity(self):
        """
        Reset the sensitivity_score and flag
        since the score has not been calculated 
        when the file has been changed 
        """
        self.flag = False
        self.sensitivity_score = 0

    @property
    def filename(self):
        return self.file.name.split('/')[1]

    @property
    def filepath(self):
        components = self.file.url.split('/')
        path = os.path.join("..", "media_root", components[2], components[3])
        return path

    @property
    def filesize(self):
        return f"{self.file.size} B"




