from django.db import models
from tinymce.models import HTMLField

class blog(models.Model):
	title = models.CharField(max_length=1024, default='')
	content = HTMLField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title