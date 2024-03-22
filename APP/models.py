from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
import os
# Create your models here.

MALE = 'M'
FEMALE = 'F'

GENDER_CHOICES = [(MALE, 'Male'), (FEMALE, 'Female'),]


def saveCertificate(request,filename):
    oldfileName= filename
    currentTime = datetime.now()
    newFileName = f'{currentTime}{oldfileName}'

    return os.path.join('certificates/',newFileName)

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Departments(models.Model):
    department = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self) -> str:
        return self.department


class Years(models.Model):
    year = models.IntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return str(self.year)


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    rollNumber = models.CharField(max_length=10, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    dep = models.ForeignKey(Departments, on_delete=models.CASCADE)
    year = models.ForeignKey(Years, on_delete=models.CASCADE)
    batch = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.user.username


class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dep = models.ForeignKey(Departments, on_delete=models.CASCADE)
    year = models.ForeignKey(Years, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Applications(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.TextField(blank=False, null=False, max_length=300)
    status = models.BooleanField(blank=False, null=False, default=False)
    rejected = models.BooleanField(blank=False, null=False, default=False)
    appliedDate = models.DateField(auto_now_add=True)
    certificateFile = models.FileField(upload_to='certificates/', blank=False)
    rejectReson = models.TextField(blank=False, null=False, max_length=300)

    def __str__(self):
        return self.student.rollNumber

