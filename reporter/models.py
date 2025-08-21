from django.db import models

class Incident(models.Model):
    INCIDENT_TYPES = [
        ('fall', 'Fall'),
        ('medication', 'Medication Error'),
        ('behavioral', 'Behavioral'),
        ('equipment', 'Equipment Failure'),
        ('infection', 'Infection Control'),
        ('injury', 'Injury'),
        ('other', 'Other'),
    ]

    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPES)
    description = models.TextField()
    reporter = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_incident_type_display()} by {self.reporter} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
