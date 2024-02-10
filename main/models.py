from django.db import models

from users.models import IMUser, Cohort

# Create your models here.

class Course(models.Model):
    name=models.CharField(default="", max_length=100)
    description=models.TextField(default='', blank=True, null=True)
    date_created=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated=models.DateTimeField(auto_now=True, blank=True, null=True)

    def str(self):
        return f"{self.name}"
    
class ClassSchedule(models.Model):
    title=models.CharField(default="", max_length=200)
    description=models.TextField(default='', max_length=1000, blank=True, null=True)
    start_date_and_time=models.DateTimeField(blank=True, null=True)
    end_date_and_time=models.DateTimeField(blank=True, null=True)
    is_repeated = models.BooleanField(default=True)
    repeat_frequency = models.CharField(default="50", max_length=1000)
    is_active = models.BooleanField(default=True)
    organizer = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='classschedule_organizer')
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='classschedule_cohort')
    venue = models.CharField(default="", max_length=100)
    date_created=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified=models.DateTimeField(auto_now=True, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classschedule_course')

    def __str__(self):
        return f"{self.title}"

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, related_name='classattendance_classschedule')
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='classattendance_member')
    is_present = models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified=models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='classattendance_author')

    def __str__(self):
        return f"{self.class_schedule} {self.member}"
    
class Query(models.Model):

    class Status(models.TextChoices):
        PENDING = 'PENDING'
        IN_PROGRESS = 'IN_PROGRESS'
        DECLINED = 'DECLINED'
        RESOLVED = 'RESOLVED'

    title=models.CharField(default="", max_length=200)
    description=models.TextField(default='', max_length=1000, blank=True, null=True)
    submitted_by=models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='queries_submitted_by')
    resolution_status = models.CharField(choices=Status.choices, max_length=100, default=Status.PENDING)
    date_created=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified=models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='queries_author')

    def __str__(self):
        return f"{self.title}"
    
class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='comments_query')
    comment=models.TextField(default='', max_length=1000, blank=True, null=True)
    date_created=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified=models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='comments_author')

    def __str__(self):
        return f"{self.query} {self.comment}"
