from django.db import models

# Create your models here.


from django.db import models
from ckeditor.fields import RichTextField
class Editor(models.Model):
    body=RichTextField(blank=True,null=True)