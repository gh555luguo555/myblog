from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=25)
    img = models.ImageField(upload_to='img/%Y/%m/%d')
    des = RichTextUploadingField(config_name='default_ckeditor', verbose_name=u'描述')
