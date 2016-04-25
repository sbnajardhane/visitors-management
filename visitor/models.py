from __future__ import unicode_literals
from datetime import datetime,timedelta
from django.db import models

    
class Person(models.Model):
	person_id = models.CharField(primary_key=True, max_length=255) 
	id_type = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	sex = models.CharField(max_length=255)
	mobile_no = models.CharField(max_length=255, default="None", blank=True)
	email_id = models.CharField(max_length=255, default="None", blank=True)
	def __str__(self):              
        	return self.name

class Visitor(models.Model):
	person_id = models.CharField(max_length=255)
	date = models.DateTimeField(max_length=255, default=datetime.now())
	intime = models.DateTimeField(max_length=255, default=datetime.now, blank=True)
	outtime = models.DateTimeField(max_length=255, default=datetime.now, blank=True)
	to_whom = models.CharField(max_length=512)
	purpose = models.CharField(max_length=512)

class Staff(models.Model):
	person_id = models.CharField(primary_key=True, max_length=255) 
	department = models.CharField(max_length=255)
	location = models.CharField(max_length=255)
	staff_type = models.CharField(max_length=255)

class Comment(models.Model):
	person_id = models.CharField(max_length=255) 
	comment = models.CharField(max_length=255)
	date = models.DateTimeField(max_length=255, default=datetime.now())

class Event(models.Model):
	event_id = models.CharField(primary_key=True, max_length=255)
	location =  models.CharField(max_length=255)
	event_name =  models.CharField(max_length=255)
	organiser =  models.CharField(max_length=255)
	date = models.DateTimeField(blank=True)
	
class Data(models.Model):
	date = models.DateTimeField(default=datetime.now())
	file_name = models.FileField(default='')
	uploader =  models.CharField(max_length=255, blank=True)
	