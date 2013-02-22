from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout_then_login
from .views import HomeTemplateView, FBchannelView
from quizz.views import ReportFormView, SupporterFormView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dreamfunder.views.home', name='home'),
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^fb_channel.html$', FBchannelView.as_view()),
    url(r'^home$', HomeTemplateView.as_view()),
    url(r'^report$', ReportFormView.as_view()),
    url(r'^supporter$', SupporterFormView.as_view()),
    #(r'^cache/', include('django_memcached.urls')),
    # url(r'^dreamfunder/', include('dreamfunder.foo.urls')),
    url(r'', include('social_auth.urls')),
    (r'^browserid/', include('django_browserid.urls')),
    (r'^avatar/', include('avatar.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    (r'^logout/?$', logout_then_login),
    (r'^complete/$', 'django.contrib.auth.views.logout',
                                                {'next_page': '/home#ThankYou'}),
)
