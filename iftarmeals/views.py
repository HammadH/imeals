from django.shortcuts import render_to_response
from django.views.generic import View, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from meal.models import Meal, Order
from users.forms import UserForm
from users.models import User


class MealsView(View):
	def get(self, request, *args, **kwargs):
		return render_to_response('index.html', {'object_list': Meal.objects.all()})
	

mealslist = MealsView.as_view()


class ProcessOrder(View):
	def get(self, request, *args, **kwargs):
		context = {}
		context['form'] = UserForm()
		context['item'] = Meal.objects.get(id=int(kwargs['id']))
		return render_to_response('order.html', context, RequestContext(request))

	def post(self, request, *args, **kwargs):
		
		form = UserForm(request.POST)
		
		if form.is_valid():
			try:
				user = User.objects.get(username=form.cleaned_data['username'])
			except User.DoesNotExist:
				user = User.objects.create(**form.cleaned_data)
			meal = Meal.objects.get(id=kwargs['id'])
			count = request.POST.get('quant[1]')
			try:
				count = int(count)
			except:
				count = 1
			order = Order(user=user, meal=meal, count=count)
			order.save()
			return HttpResponseRedirect(reverse('order_success'))
		else:
			context = {}
			context['item'] = Meal.objects.get(id=int(kwargs['id']))
			context['form'] = form
			return render_to_response('order.html', context, RequestContext(request))

process_order = ProcessOrder.as_view()

class OrderSuccess(TemplateView):
	template_name = 'order_success.html'

order_success = OrderSuccess.as_view()