
from django.db import models


class ticklist(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title

