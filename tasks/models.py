from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING_REVIEW', 'Pending Review'),
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    tags = models.JSONField(default=list, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='OPEN')

    def save(self, *args, **kwargs):
        # Ensure unique tags
        self.tags = list(set(self.tags))
        if self.due_date and self.due_date < now().date():
            self.status = 'OVERDUE'
        super().save(*args, **kwargs)
