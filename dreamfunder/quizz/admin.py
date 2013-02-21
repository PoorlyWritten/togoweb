from django.contrib import admin

from .models import Quizz, Question, AnswerChoice

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'text', 'comment', 'image_letter']
    list_editable = ['text', 'comment', 'image_letter']
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'question', 'order', 'answers']
    list_editable = ['name', 'question', 'order']

    def answers(self, instance):
        return len(instance.answerchoice_set.all())

admin.site.register(Quizz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(AnswerChoice, AnswerAdmin)
