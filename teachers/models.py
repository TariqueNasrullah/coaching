from django.db import models

class teacher(models.Model):
	name = models.CharField(max_length=256)
	subject = models.CharField(max_length=256)
	teacher_photo = models.ImageField(upload_to='imageFiles', blank=True)
	facebook_profile = models.CharField(max_length=1024, blank=True)
	instagram_profile = models.CharField(max_length=1024, blank=True)
	twitter_profile = models.CharField(max_length=1024, blank=True)
	googlePlus_profile = models.CharField(max_length=1024, blank=True)

	def __str__(self):
		return self.name