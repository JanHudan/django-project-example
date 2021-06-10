from django.db import models

class TesterModel(models.Model):
    name = models.TextField(null=False, default=None)
    email = models.TextField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class CompanyModel(models.Model):
    name = models.TextField(null=False, default=None)

    def __str__(self):
        return self.name

class ProjectModel(models.Model):
    name = models.TextField(null=False, default=None)
    company = models.ForeignKey(
        CompanyModel,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name

class HardwareModel(models.Model):
    tester = models.ForeignKey(
        TesterModel,
        on_delete=models.SET_NULL,
        null=True,
    )
    project = models.ForeignKey(
        ProjectModel,
        on_delete=models.SET_NULL,
        null=True,
    )
    name = models.TextField(null=False, default=None)

    STATUS_CHOICES = [
        ('Unassigned', 'Unassigned'),
        ('To be delivered', 'To be delivered'),
        ('Delivered', 'Delivered'),
        ('Returning', 'Returning'),
        ('Returned', 'Returned'),
        ('Kept', 'Kept')
    ]

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Unassigned')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name