"""
models
"""

from django.db import models

# Create your models here.


class TimeBlock(models.Model):
    """
    a time block contains a duration [start_datetime: end_datetime) (not include the end_datetime)
    """
    object_id = models.TextField(index=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
