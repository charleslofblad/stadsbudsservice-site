from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
# For Django 1.9.3.

class Article(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    
    def __unicode__(self):
        return '%s' % self.title
    
    @permalink
    def get_absolute_url(self):
        return ('view_article_post', None, { 'slug': self.slug })