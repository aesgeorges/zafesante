from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Questions(models.Model):
    question = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=50)
    votes = models.IntegerField(default='0')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
            ordering = ['created']

    def __unicode__(self):
            return u'%s' % self.question

    def get_absolute_url(self):
            return reverse('single_question', args=[self.slug])


class Voted(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
