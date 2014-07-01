from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iftarmeals.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^create/', 'restaurant.views.create', name='create_restaurant' ),
	# url(r'^edit/', ),
	# url(r'^delete/', ),
)




urlpatterns += staticfiles_urlpatterns()