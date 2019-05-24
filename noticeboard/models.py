from django.db import models
from django.core.exceptions import ValidationError

def fileValidation_extension(value):
	if not value.name.endswith('.pdf'):
		raise ValidationError(u'Upload a pdf file')

class notice(models.Model):
	notice_title = models.CharField(max_length=1024, blank=False)
	notice_pdf_file = models.FileField(upload_to='noticeFiles/', blank=False, validators=[fileValidation_extension])
	date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.notice_title