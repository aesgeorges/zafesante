from django.db import models
from django.urls import reverse
# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=255)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    content = models.TextField()
    picture = models.ImageField('img', upload_to='pictures/', blank=True)
    featured = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
            ordering = ['created']

    def __unicode__(self):
            return u'%s' % self.title

    def get_absolute_url(self):
            return reverse('single_article', args=[self.slug])
