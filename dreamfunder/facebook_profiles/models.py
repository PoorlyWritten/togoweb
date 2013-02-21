from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields.json import JSONField
from  facepy import GraphAPI

class FacebookProfile(models.Model):
    user = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now_add=True)
    friends = JSONField()
    interests = JSONField()
    details = JSONField()
    access_token = models.CharField(max_length=256)

    def get_conn(self):
        try:
            return self.fb_conn
        except AttributeError:
            self.fb_conn = GraphAPI(self.access_token)
            return self.fb_conn

    def get_details(self):
        graph = self.get_conn()
        detail = graph.get('me', fields=[
            'friends',
            'interests'])
        self.friends = detail['friends']['data']
        try:
            self.interests = detail['interests']['data']
        except KeyError:
            self.interests = ''
        self.save()
        print detail.keys()

