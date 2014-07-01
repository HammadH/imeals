from django.db import models
from django.contrib import admin

from sorl.thumbnail import ImageField

def get_logo_path(instance, filename):
	import pdb;pdb.set_trace()
	return "media/Restaurant_images/%s/Logos/%s" %(instance, filename)

class Restaurant(models.Model):
	name = models.CharField(
		'Name of restaurant', max_length=100, null=False, blank=False)
	logo = ImageField(upload_to=get_logo_path, blank=True, null=True)
	address = models.TextField(blank=False)
	phone = models.CharField(max_length=10, blank=False)
	email = models.EmailField(blank=False)
	website = models.URLField(blank=True, null=True)
	zomato = models.URLField(blank=True, null=True)


	def __unicode__(self):
		return self.name




admin.site.register(Restaurant)