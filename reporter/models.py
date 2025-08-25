from django.db import models

class Incident(models.Model):
    INCIDENT_TYPES = [
        ('Fall', 'Fall'),
        ('Medication', 'Medication Error'),
        ('Behavioral', 'Behavioral'),
        ('Equipment', 'Equipment Failure'),
        ('Infection', 'Infection'),
        ('Injury', 'Injury'),
        ('Other', 'Other'),
    ]

    SEVERITY_LEVELS = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)  # Date & Time
    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPES)  # Type
    severity = models.CharField(max_length=10, choices=SEVERITY_LEVELS)  # Severity
    location = models.CharField(max_length=255)  # Location
    resident = models.CharField(max_length=255)  # Resident
    description = models.TextField()  # Description
    reporter = models.CharField(max_length=255)  # Reporter
    incident_date_time = models.DateTimeField(null=True, blank=True)  # Incident Date & Time
    reported_to_manager = models.BooleanField(default=False)  # Reported to Manager
    actions_taken = models.TextField(null=True, blank=True)  # Actions Taken

    class Meta:
        ordering = ['-timestamp'] 

    def __str__(self):
        return f"{self.get_incident_type_display()} - {self.get_severity_display()} at {self.timestamp:%d-%m-%Y-%H:%M}"