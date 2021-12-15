from django.db import models

class Employee(models.Model):
	id = models.IntegerField(primary_key=True)	#序号
	name = models.CharField(max_length=30)		#名字
	mobile = models.CharField(max_length=20)	#手机号
	hire_date = models.DateTimeField()			#入职时间

