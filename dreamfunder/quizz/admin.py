from django.contrib import admin

from .models import Quizz, Question, AnswerChoice

admin.site.register(Quizz)
admin.site.register(Question)
admin.site.register(AnswerChoice)
