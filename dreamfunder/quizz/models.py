from django.db import models
from django.contrib.auth.models import User
import os

def upload_file_path(instance=None, filename=None):
    tmppath = 'answer_images'
    if not filename:
        # Filename already stored in database
        filename = instance.image.name
    tmppath.append(os.path.basename(filename))
    return os.path.join(*tmppath)

class Quizz(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    quizz = models.ForeignKey(Quizz)
    name = models.CharField(max_length=256)
    question = models.CharField(max_length=1024)
    order = models.IntegerField()

    def __unicode__(self):
        return self.name

class AnswerChoice(models.Model):
    question = models.ForeignKey(Question)
    image = models.ImageField(max_length=1024, upload_to=upload_file_path, blank=True)
    text = models.CharField(max_length=256)
    comment = models.CharField(max_length=1024)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

class QuizzProfile(models.Model):
    user = models.ForeignKey(User)
    quiz_started = models.DateTimeField(auto_now_add=True)
    quiz_completed = models.DateTimeField(blank=True)
    quiz_answers = models.ManyToManyField(AnswerChoice)
