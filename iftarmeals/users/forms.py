import re
from django import forms
from django.utils.translation import ugettext_lazy as _

from users.models import User

def validate_mobile(mobile):
	format = re.compile('[0]{1}[0-9]{9}')
	if re.match(format, mobile) != None:
		return True
	return False

class UserForm(forms.Form):
	username = forms.CharField(label=_('Full Name'), required=True)
	email = forms.CharField(label=_('Email'), required=True	)
	mobile = forms.CharField(label=_('Mobile'), required=True)
	address = forms.CharField(label=_('Address'), widget=forms.Textarea (attrs={'rows':3}))


	def clean_mobile(self):
		mobile = self.cleaned_data['mobile']
		if validate_mobile(mobile):
			return mobile
		else:
			raise forms.ValidationError("Invalid mobile number!")

		
			


		