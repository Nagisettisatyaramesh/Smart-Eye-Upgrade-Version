from django.db import models


class Lead(models.Model):
    class CompanySize(models.TextChoices):
        SMALL = '1-50', '1-50 employees'
        MEDIUM = '51-200', '51-200 employees'
        LARGE = '201-1000', '201-1000 employees'
        ENTERPRISE = '1000+', '1000+ employees'

    name = models.CharField(max_length=150)
    email = models.EmailField()
    company = models.CharField(max_length=150)
    phone = models.CharField(max_length=30, blank=True)
    company_size = models.CharField(
        max_length=20, choices=CompanySize.choices, blank=True
    )
    interest = models.CharField(max_length=150, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} ({self.company})'
