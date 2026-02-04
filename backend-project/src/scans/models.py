from django.db import models
from jobs.models import Job


class ScanResult(models.Model):
    job = models.OneToOneField(
        Job,
        on_delete=models.CASCADE,
        related_name="result"
    )
    data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
