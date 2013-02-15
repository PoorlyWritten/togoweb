# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quizz'
        db.create_table('quizz_quizz', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('quizz', ['Quizz'])

        # Adding model 'Question'
        db.create_table('quizz_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quizz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quizz.Quizz'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('quizz', ['Question'])

        # Adding model 'AnswerChoice'
        db.create_table('quizz_answerchoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quizz.Question'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=1024, blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('date_uploaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('quizz', ['AnswerChoice'])


    def backwards(self, orm):
        # Deleting model 'Quizz'
        db.delete_table('quizz_quizz')

        # Deleting model 'Question'
        db.delete_table('quizz_question')

        # Deleting model 'AnswerChoice'
        db.delete_table('quizz_answerchoice')


    models = {
        'quizz.answerchoice': {
            'Meta': {'object_name': 'AnswerChoice'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'date_uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '1024', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quizz.Question']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'quizz.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'quizz': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quizz.Quizz']"})
        },
        'quizz.quizz': {
            'Meta': {'object_name': 'Quizz'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['quizz']