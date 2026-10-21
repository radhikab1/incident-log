from django.db import models
from django.utils import timezone

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner_team = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Incident(models.Model):
    class Severity(models.TextChoices):
        SEV1 = "SEV1", "SEV1 - Critical"
        SEV2 = "SEV2", "SEV2 - Major"
        SEV3 = "SEV3", "SEV3 - Minor"
        SEV4 = "SEV4", "SEV4 - Low"

    class Status(models.TextChoices):
        OPEN = "open", "Open"
        INVESTIGATING = "investigating", "Investigating"
        RESOLVED = "resolved", "Resolved"

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    severity = models.CharField(
        max_length=4, choices=Severity.choices, default=Severity.SEV3
    )
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.OPEN
    )
    service = models.ForeignKey(
        Service, on_delete=models.PROTECT, related_name="incidents"
    )
    root_cause = models.TextField(blank=True)
    resolution = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"[{self.severity}] {self.title}"