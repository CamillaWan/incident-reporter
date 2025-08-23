from django.db import models

class Incident(models.Model):
    INCIDENT_TYPES = [
        ('fall', 'Fall'),
        ('medication', 'Medication Error'),
        ('behavioral', 'Behavioral'),
        ('equipment', 'Equipment Failure'),
        ('infection', 'Infection'),
        ('injury', 'Injury'),
        ('other', 'Other'),
    ]

    SEVERITY_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)  # Date & Time
    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPES)  # Type
    severity = models.CharField(max_length=10, choices=SEVERITY_LEVELS)  # Severity
    location = models.CharField(max_length=255)  # Location
    resident = models.CharField(max_length=255)  # Resident
    description = models.TextField()  # Description
    reporter = models.CharField(max_length=255)  # Reporter

    class Meta:
        ordering = ['-timestamp'] 

    def __str__(self):
        return f"{self.get_incident_type_display()} - {self.get_severity_display()} at {self.timestamp:%d-%m-%Y-%H:%M}"