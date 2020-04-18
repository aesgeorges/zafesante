from django.db import models
from django.urls import reverse
# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=100)
    title_fr = models.CharField(max_length=100, blank=True)
    title_en = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True, max_length=255)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    description_en = models.CharField(max_length=255, blank=True)
    description_fr = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    content_fr = models.TextField(blank=True)
    content_en = models.TextField(blank=True)
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


class Infocard(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)

    class Meta:
            ordering = ['created']


class InfocardImage(models.Model):
    infocard = models.ForeignKey(Infocard, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('img', upload_to='pictures/', blank=True)
