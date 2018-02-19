from django.db import models

# Create your models here.

class ContactInfo(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	message = models.TextField()
	date_time = models.DateTimeField()

	def __str__(self):
		return self.first_name + " " + self.last_name + " - " + str(self.date_time)

