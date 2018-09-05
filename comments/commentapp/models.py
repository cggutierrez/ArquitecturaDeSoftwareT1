from django.db import models


class Comment(models.Model):
    text = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=19)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.text

