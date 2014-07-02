from django.db import models
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string

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
	user = models.ForeignKey('users.User', blank=False, related_name='orders')
	meal = models.ForeignKey(Meal, blank=False)
	count = models.IntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return "Order:%s by %s" %(self.meal, self.user)


@receiver(post_save, sender = Order)
def meal_ordererd(sender, **kwargs):
	if kwargs['created']:
		order = kwargs['instance']
		meal_item = order.meal
		customer = order.user
		quantity = order.count
		restaurant = meal_item.restaurant
		subject = "New Order"
		message = render_to_string("order_email.txt", {'customer': customer, 'meal':meal_item, 'restaurant': restaurant, 'quantity':quantity})
		send_mail(subject, message, 'orders@iftarmeals.com', ['hammadsyed9@gmail.com', restaurant.email,], fail_silently=False)
		return
	else:
		return



admin.site.register(Meal)

admin.site.register(Order)