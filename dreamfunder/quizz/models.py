from django.db import models
from django.contrib.auth.models import User
import os
import json
from django_extensions.db.fields.json import JSONField


def upload_file_path(instance=None, filename=None):
    tmppath = ['answer_images']
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

    def as_obj(self):
        obj = dict(
            name = self.name,
            question = self.question,
            answers = []
        )
        for answer in self.answerchoice_set.all():
            try:
                obj['answers'].append(dict(
                    text = answer.text,
                    comment = answer.comment,
                    image = answer.image.url,
                    image_letter = answer.image_letter
                ))
            except ValueError:
                print answer.id
        return obj

    def as_json(self):
        return json.dumps(self.as_obj())


class AnswerChoice(models.Model):
    question = models.ForeignKey(Question)
    image = models.ImageField(max_length=1024, upload_to=upload_file_path, blank=True)
    text = models.CharField(max_length=256)
    comment = models.CharField(max_length=1024)
    image_letter = models.CharField(max_length=3, default="A")
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

class QuizzProfile(models.Model):
    HONEYMOON = 'HONEYMOON'
    GRADUATION = 'GRADUATION'
    BIRTHDAY = 'BIRTHDAY'
    QUINCEANERA = 'QUINCEANERA'
    ANNIVERSARY = 'ANNIVERSARY'
    GAPYEAR = 'GAPYEAR'
    RETIREMENT = 'RETIREMENT'
    OTHER = 'OTHER'
    EVENT_CHOICES = (
        (HONEYMOON,'Honeymoon/Wedding'),
        (GRADUATION,'Graduation'),
        (BIRTHDAY,'Birthday'),
        (QUINCEANERA,'Quinceanera/Debutante'),
        (ANNIVERSARY,'Anniversary'),
        (GAPYEAR,'Gap Year/Sabbatical'),
        (RETIREMENT,'Retirement'),
        (OTHER,'Other Special Occasion'),
    )

    CHILD = 'CHILD'
    PARENT = 'PARENT'
    PARTNER = 'PARTNER'
    ME      = 'ME'
    FRIEND = 'FRIEND'
    FAMILY  = 'FAMILY'
    RELATIONSHIP_CHOICES = (
        (CHILD,'My Son'),
        (CHILD,'My Daughter'),
        (PARENT,'My Mother'),
        (PARENT,'My Father'),
        (PARTNER,'My Wife'),
        (PARTNER,'My Husband'),
        (PARTNER,'My Partner'),
        (FRIEND,'My Friend'),
        (FAMILY,'Another Family Member'),
        (ME,'My Self!'),
    )
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    quiz_started = models.DateTimeField(auto_now_add=True)
    quiz_completed = models.DateTimeField(blank=True, null=True)
    quiz_answers = JSONField()
    quiz_relationship = models.CharField(max_length=32, choices=RELATIONSHIP_CHOICES, null=True, blank=True)
    quiz_event = models.CharField(max_length=32, choices=EVENT_CHOICES, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
