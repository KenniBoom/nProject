from django.db import models

# Kuriamas modelis

class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default='Aprasymas')
    keywords = models.CharField(max_length=120, default='Raktiniai zodziai')
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    visible = models.BooleanField(default=1)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
 
    def __unicode__(self):
        return self.title
 
    def __str__(self):
        return self.title
 
    def get_absolute_url(self):
        return "/%s/" %(self.id)
 
    class Meta:
        ordering = ["-id", "-timestamp"]

# Create your models here.
