from django.db import models

class event(models.Model):
	title = models.CharField(max_length=1200, blank=False)
	date = models.DateField(blank=False)
	location = models.CharField(max_length=1200)
	short_description = models.TextField()
	title_image = models.ImageField(upload_to='imageFiles', blank=True)
	youtube_vide_link = models.CharField(max_length=1200, blank=True)

	def __str__(self):
		return self.title