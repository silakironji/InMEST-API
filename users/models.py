from django.db import models

# Create your models here.
    

class IMUser(models.Model):

    class UserType(models.TextChoices):
        EIT = 'EIT'
        TEACHING_FELLOW = 'TEACHING_FELLOW'
        ADMIN_STAFF = 'ADMIN_STAFF'
        ADMIN = 'ADMIN'

    first_name=models.CharField(default='',max_length=100)
    last_name=models.CharField(default='', max_length=100)
    email=models.EmailField(default='', max_length=100)
    is_active=models.BooleanField(default=True)
    user_type=models.CharField(choices=UserType.choices, max_length=100, default=UserType.EIT)
    date_created=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified=models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"
    
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
