import requests
from django.core.files.uploadedfile import SimpleUploadedFile
from social_auth.backends.facebook import FacebookBackend
from avatar.models import Avatar
from .models import FacebookProfile

def get_user_avatar(backend, details, response, social_user, uid,\
                    user, *args, **kwargs):
    url = None
    if backend.__class__ == FacebookBackend:
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']

    print response.keys()
    if url:
        print url
        avtr = Avatar(
                user = user,
                primary = True,
            )
        image_request = requests.get(url)
        print image_request.headers
        content_type=image_request.headers['content-type']
        print content_type
        filename = user.username
        if content_type == 'image/jpeg':
            filename = "%s.jpg" % user.username
        if content_type == 'image/png':
            filename = "%s.png" % user.username
        image_file = SimpleUploadedFile(
            filename,
            image_request.content,
            content_type=content_type
        )
        print image_file.__dict__
        avtr.avatar.save(image_file.name, image_file)
        avtr.save()


def get_details(backend, details, response, social_user, uid,\
                    user, *args, **kwargs):
    profile = FacebookProfile(
                user = user,
                access_token = response['access_token']
    )
    profile.get_details()
