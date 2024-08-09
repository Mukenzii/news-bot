from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    link = models.URLField()
    date = models.CharField(max_length=50,null=True,blank=True)
    visibility = models.CharField(max_length=12,null=True)


    def __str__(self):
        return self.title

