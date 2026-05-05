from django.db import models

class Employee(models.Model):
    employeeId = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    salary = models.FloatField()
    departmentID = models.IntegerField()

    def __str__(self):
        return self.fullName