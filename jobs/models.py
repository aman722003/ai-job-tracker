from django.db import models

from django.conf import settings


class JobApplication(models.Model):

    STATUS_CHOICES = [

        ('Applied', 'Applied'),

        ('Interview', 'Interview'),

        ('Rejected', 'Rejected'),

        ('Offer', 'Offer'),
    ]

    user = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE
    )

    company_name = models.CharField(
        max_length=255
    )

    role = models.CharField(
        max_length=255
    )

    status = models.CharField(

        max_length=50,

        choices=STATUS_CHOICES,

        default='Applied'
    )

    salary = models.IntegerField(
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    resume = models.FileField(

        upload_to='resumes/',

        blank=True,

        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    extracted_skills = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):

        return f"{self.company_name} - {self.role}"