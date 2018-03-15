from django.db import models
from django.urls import reverse
import datetime
# Create your models here.


class Video(models.Model):
    name = models.CharField(max_length=255, default='vid')
    slug = models.SlugField(unique=True, max_length=255, default='slug')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()
    created = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name

    class Meta:
            ordering = ['created']

    def __unicode__(self):
            return u'%s' % self.video

    def get_absolute_url(self):
            return reverse('video', args=[self.slug])
