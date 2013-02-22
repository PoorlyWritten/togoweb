import logging
logger = logging.getLogger(__name__)
# Create your views here.
from django.views.generic.edit import FormView
from .models import Question, QuizzProfile
from .forms import ReportForm, SupporterForm
import json
import datetime
from django.utils.timezone import utc


class QuestionsJsonMixin(object):

    def get_context_data(self, **kwargs):
        context = super(QuestionsJsonMixin, self).get_context_data(**kwargs)
        questions = Question.objects.all()
        questions_obj = {}
        for each in questions:
            questions_obj[each.name] = each.as_obj()
        context['questions_json'] = json.dumps(questions_obj)
        return context



class ReportFormView(FormView):
    success_url = '/complete'
    form_class = ReportForm

    def form_valid(self, form):
        logger.info("%s - %s" % (self.request.user.email, form.cleaned_data['report']))
        return super(ReportFormView, self).form_valid(form)

class SupporterFormView(FormView):
    success_url = '/complete'
    form_class = SupporterForm

    def form_valid(self, form):
        kwargs = form.cleaned_data
        if self.request.user.is_authenticated():
            logger.info("%s - %s" % (self.request.user.email, form.cleaned_data))
            kwargs['user'] = self.request.user
        else:
            logger.info("%s - %s" % (self.request.user, form.cleaned_data))
        try:
            obj = QuizzProfile.objects.get(**kwargs)
        except QuizzProfile.DoesNotExist:
            obj = QuizzProfile(**dict((k,v) for (k,v) in kwargs.items() if '__' not in k))
        obj.quiz_completed = datetime.datetime.utcnow().replace(tzinfo=utc)
        obj.save()

        return super(SupporterFormView, self).form_valid(form)


