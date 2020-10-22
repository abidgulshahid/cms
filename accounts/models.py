from django.db import models

# Create your models here.


class BSCS(models.Model):

	class_schedule = models.CharField(max_length=200,null=True)
	course_work = models.CharField(max_length=200,null=True)
	sem = models.CharField(max_length=10,null=True)
	subject_teacher = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.course_work

class students_courses(models.Model):
	pass

