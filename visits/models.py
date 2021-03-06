from django.db import models

from users.models import Doctor, Patient


class Visit(models.Model):
    doctor = models.ForeignKey('users.Doctor', null=True, blank=True, on_delete=models.CASCADE)
    patient = models.ForeignKey('users.Patient', null=True, blank=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, default='')
    price = models.FloatField(default=0.0)
    date = models.DateTimeField(default='')

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.doctor, self.address, self.date
