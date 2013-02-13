from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout_then_login
from .views import HomeTemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dreamfunder.views.home', name='home'),
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^home$', HomeTemplateView.as_view()),
    # url(r'^dreamfunder/', include('dreamfunder.foo.urls')),
    url(r'', include('social_auth.urls')),
    (r'^browserid/', include('django_browserid.urls')),
    (r'^avatar/', include('avatar.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    (r'^logout$', logout_then_login),
)
