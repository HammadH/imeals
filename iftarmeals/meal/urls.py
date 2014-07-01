from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iftarmeals.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(?P<id>[0-9])/', 'meal.views.meal_detail', name='meal_detail_view' ),
	# url(r'^edit/', ),
	# url(r'^delete/', ),
)

