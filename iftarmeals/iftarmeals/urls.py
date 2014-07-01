from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static 

from django.contrib import admin
admin.autodiscover()

from views import mealslist, process_order, order_success

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iftarmeals.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', mealslist, name = 'mealslist'),

    url(r'^restaurant/', include('restaurant.urls')),
    url(r'^meal/', include('meal.urls')),
    url(r'^order/(?P<id>[0-9])/', process_order, name = 'process_order' ),
    url(r'^order_sucess/', order_success, name='order_success'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()