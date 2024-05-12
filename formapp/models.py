from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name if self.active else f"{self.name} (inactive)"


class Contracts(models.Model):
    name = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
