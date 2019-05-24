from django.db import models

SUBJECT_CHOICES = ( ('Science', 'SCINECE'), ('Commerce', 'COMMERCE'), ('Arts', 'ARTS'), ('All Subject', 'ALL SUBJECT'),)

class free_materials(models.Model):
	title = models.CharField(max_length=1024, blank=False)
	file = models.FileField(upload_to='studymaterials/freematerials', blank=False)
	belongs_to = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='Science')
	date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title