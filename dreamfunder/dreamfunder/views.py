from django.views.generic import TemplateView
from quizz.views import QuestionsJsonMixin

class HomeTemplateView(QuestionsJsonMixin, TemplateView):
    template_name = "home.html"

class FBchannelView(TemplateView):
    template_name = "fb_channel.html"
