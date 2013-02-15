from django.views.generic import TemplateView

class HomeTemplateView(TemplateView):
    template_name = "home.html"

class FBchannelView(TemplateView):
    template_name = "fb_channel.html"
