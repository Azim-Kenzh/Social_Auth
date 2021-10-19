from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from account.models import MyUser
from core import settings
from oauth.serializers import GoogleAuthSerializer
from oauth.services import base_auth


def check_google_auth(google_user: GoogleAuthSerializer) -> dict:
    try:
        id_token.verify_oauth2_token(google_user['token'], requests.Request(), settings.GOOGLE_CLIENT_ID)
    except ValueError:
        raise AuthenticationFailed(code=403, detail='Bad token Google')

    user, _ = MyUser.objects.get_or_create(email=google_user['email'], defaults={
        'first_name': google_user['first_name'], 'last_name': google_user['last_name']
    })
    return base_auth.create_token(user.id)