from django.db import models
from django.utils import timezone
from custom_user.models import BugUser

class Ticket(models.Model):
    title = models.CharField(max_length=60, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    bug = models.TextField()
    username = models.ForeignKey(BugUser, on_delete=models.CASCADE,
        related_name="user_name")

    NEW = "NE"
    IN_PROGRESS = "IP"
    DONE = "DO"
    INVALID = "IN"

    TICKET_STATUS_CHOICES = [
        (NEW, "new"),
        (IN_PROGRESS, "in progress"),
        (DONE, "done"),
        (INVALID, "invalid")
    ]

    ticket_status = models.CharField(
        max_length=2,
        choices=TICKET_STATUS_CHOICES,
        default=NEW
    )

    assigned_user = models.ForeignKey(BugUser, on_delete=models.CASCADE,
        related_name="assigned", null=True, blank=True)
    completed_by = models.ForeignKey(BugUser, on_delete=models.CASCADE,
        related_name="completed", null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.bug}"
