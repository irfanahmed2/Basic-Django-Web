from django.db import models

# Create your models here.

class member(models.Model):
	name = models.CharField(max_length=10)
	last_name = models.CharField(max_length=10)
	email = models.CharField(max_length=25)

	def __str__(self):
		return self.name + self.last_name