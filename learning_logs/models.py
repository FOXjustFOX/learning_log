from django.db import models

# Create your models here.


class Topic(models.Model):
    """toppic defined by user"""
    text = models.CharField(max_length=100)
    desc = models.CharField(max_length=250, default="")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns model representation in a str form"""
        return self.text

class Entry(models.Model):
    """exact info about progress in learning"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    desc = models.TextField(default="")
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entries'

        
    def __str__(self):
        return self.text[:50] if len(self.text) > 50 else self.text
