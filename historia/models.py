from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from datetime import datetime

# Create your models here.
class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="title")
    date = models.DateTimeField()
    body = models.TextField()
    dm_only = models.TextField(null=True, blank=True)
    record = models.FileField( upload_to="records", blank=True)

    class Meta:
        ordering = ("-date",)
    
    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse("historia:detail", kwargs={"slug": self.slug})