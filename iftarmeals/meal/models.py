from django.db import models
from django.contrib import admin

from restaurant.models import Restaurant

from sorl.thumbnail import ImageField

def get_meal_image_path(instance, filename):
	return "media/Restaurant_images/%s/%s/%s" %(instance.restaurant, instance, filename)

class Meal(models.Model):
	name = models.CharField("Name of combo meal", max_length=100)
	price = models.IntegerField(blank=False, null=False)
	image_1 = ImageField(upload_to=get_meal_image_path)
	image_2 = ImageField(upload_to=get_meal_image_path)
	image_3 = ImageField(upload_to=get_meal_image_path)
	description = models.TextField(blank=False)
	delivery_time = models.CharField(max_length=50, blank=False)
	restaurant = models.ForeignKey(Restaurant, blank=False, related_name='meals')

	def __unicode__(self):
		return self.name



class Order(models.Model):
	user = models.OneToOneField('users.User', blank=False, related_name='orders')
	meal = models.OneToOneField(Meal, blank=False)
	count = models.IntegerField(default=1)

	def __unicode__(self):
		return "Order:%s by %s" %(self.meal, self.user)

admin.site.register(Meal)

admin.site.register(Order)