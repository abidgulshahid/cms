from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class BS(models.Model):

	class_schedule = models.CharField(max_length=200,null=True)
	course_work = models.CharField(max_length=200,null=True)
	sem = models.CharField(max_length=10,null=True)
	subject_teacher = models.CharField(max_length=200,null=True)

	def __str__(self):
            return self.course_work


class announcments(models.Model):
        msg = models.CharField(max_length=200, null=True)
        date = models.DateField(null=True)
     #   date = models.DateField(default=datetime.date.today)
        
        def __str__(self):
            return self.msg

class student_registration(models.Model):
   full_name = models.CharField(max_length=30,null=True)
   username = models.CharField(max_length=30,null=True)
   email = models.EmailField(verbose_name='Enter Your Email:',max_length=50, null=True)
   password = models.CharField(max_length=30,null=True)
   semester = models.DecimalField(verbose_name="Semester:",max_digits=2,decimal_places=1)
   created_at = models.DateField(auto_created=True,)

   def __str__(self):
      return self.full_name

class students_courses(models.Model):
	pass



class CustomUser(AbstractUser):
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    # add additional fields in here

    def __str__(self):
        return self.username
