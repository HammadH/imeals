from django.shortcuts import render_to_response
from django.views.generic import View
from django.http import HttpResponse

from meal.models import Meal



class MealDetailView(View):
	def get(self, request, *args, **kwargs):
		meal = Meal.objects.get(id=kwargs['id'])
		restaurant = meal.restaurant
		return render_to_response('meal_detail.html', {'item': meal,
			'restaurant' : restaurant})

meal_detail = MealDetailView.as_view()

