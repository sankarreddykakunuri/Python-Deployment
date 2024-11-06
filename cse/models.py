from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], default='M')
    date_of_birth = models.DateField(null=True, blank=True)  # Allows for empty values

    def __str__(self):
        return self.name
