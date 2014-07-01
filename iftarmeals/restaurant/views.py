from django.http import HttpResponseRedirect

from django.views.generic import FormView

from .models import Restaurant
from .forms import RestaurantForm
from .mixins import LoginRequiredMixin


class RestaurantCreateView( FormView):
	form_class = RestaurantForm
	template_name = 'restaurantform.html'
	success_url = '/'

	def form_valid(self, form):
		Restaurant(**form.cleaned_data).save()
		return HttpResponseRedirect(self.get_success_url())



create = RestaurantCreateView.as_view()

