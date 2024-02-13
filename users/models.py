from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

# Create your models here.
    

class IMUser(AbstractUser):
    first_name = models.CharField(max_length=155, blank=True)
    last_name = models.CharField(max_length=155, blank=True)
    middle_name = models.CharField(max_length=155, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)


    USER_TYPES = [
        ('EIT', 'Engineering Intern'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Administrative Staff'),
        ('ADMIN', 'Administrator'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='EIT')
    date_created = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, related_name='imuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='imuser_set')
    
    def _str_(self):
        return f"{self.first_name} {self.last_name}"
    
class Cohort(models.Model):
    name=models.CharField(default='',max_length=100)
    description=models.TextField(default='', blank=True, null=True)
    start_date=models.DateTimeField(blank=True, null=True)
    end_date=models.DateTimeField(blank=True, null=True)
    date_created=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified=models.DateTimeField(auto_now=True, blank=True, null=True)
    year=models.IntegerField(default=2024)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohorts_author')

    def __str__(self):
        return f"{self.name}"
    
class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='members')
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohortmembers_member')
    is_active = models.BooleanField(default=True)
    date_created=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified=models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohortmembers_author')
