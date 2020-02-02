from __future__ import unicode_literals
from django.db import models
from registeration.models import Profile
from django.contrib.auth.models import User
from django import template

register = template.Library()

class Job(models.Model):
    title = models.CharField(max_length = 150 , blank = False)
    description = models.CharField(max_length = 150 , blank = False)
    location = models.CharField(max_length = 150 , blank = False)
    createdBy = models.ForeignKey(User,on_delete = models.CASCADE)

    @property
    def is_applied(self,job_id):
        print(job_id)
        # Jobinstance = JobsApplication.objects.filter(Job = self.Id,Applicant = request.user)
        return True

    def __str__(self):
        return self.title  + ' -- ' + self.location + '--' + self.createdBy.username

    @register.simple_tag
    def related_deltas(self):
        return True

class JobsApplication(models.Model):
    Job = models.ForeignKey(Job,on_delete = models.CASCADE ,null = False,blank=False)
    Applicant = models.ForeignKey(User,on_delete = models.CASCADE,null = False,blank=False )
    postedby = models.ForeignKey(User,on_delete = models.CASCADE,related_name = "recruiter",null = False,blank=False )

    def getAllApplicants(self):
        pass

    def __str__(self):
        return self.Job.title + '---' + self.Applicant.username + '---' + self.postedby.username
