from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Content(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(default='')

class Image(BaseModel):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    image = models.ImageField()
    order = models.SmallIntegerField()

    class Meta:
        unique_together = ['content', 'order']

