from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=1000)
    time = models.TimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
