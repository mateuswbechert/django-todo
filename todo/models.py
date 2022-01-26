from django.utils import timezone
from django.db import models

class Todo(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    status=models.ForeignKey('Status', on_delete=models.PROTECT, blank=True, default='2')
    order_id=models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title


class Status(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title



