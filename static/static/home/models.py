from django.db import models
from tinymce.models import HTMLField

class blog(models.Model):
	title = models.CharField(max_length=1024, default='')
	content = HTMLField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class contact_information(models.Model):
	name = models.CharField(max_length=100, default='')
	email = models.CharField(max_length=200, default='')
	subject = models.CharField(max_length=300, default='')
	message = models.TextField(max_length=1200, default='')

	def __str__(self):
		return self.subject
