from django.utils import timezone
from django.db import models
from django.conf import settings

class Todo(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    status=models.ForeignKey('Status', on_delete=models.PROTECT, blank=True, default='2')
    order_id=models.IntegerField(blank=True, default=0)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Status(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Board(models.Model):
    title=models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


# class BoardUser(models.Model):
#     board_id=models.ForeignKey('Board', on_delete=models.PROTECT)
#     user_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     user_board_id=models.IntegerField(default=0)


# class CardUser(models.Model):
#     card_id=models.ForeignKey('Todo', on_delete=models.PROTECT)
#     user_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     user_card_id=models.IntegerField(default=0)