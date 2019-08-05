from django.views.decorators.csrf import csrf_exempt
# from django.conf.settings import ACCOUNT_SID, API_KEY, API_SECRET
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from faker import Faker
import requests

fake = Faker()

ACCOUNT_SID = settings.ACCOUNT_SID
API_KEY = settings.API_KEY
API_SECRET = settings.API_SECRET

@csrf_exempt
@api_view(["GET"])
def token(request):

    # Create an Access Token
    token = AccessToken(ACCOUNT_SID, API_KEY, API_SECRET)

    # Set the Identity of this token
    # token.identity = request.values.get('identity') or 'identity'
    token.identity = fake.name()
    
    # Grant access to Video
    grant = VideoGrant()
    # grant.room = requests.get('room')
    grant.room = 'room'
    token.add_grant(grant)

    # Return token
    # return token.to_jwt()
    data = {
    	'identity': token.identity,
    	'token': token.to_jwt().decode('utf-8')
    }
    return Response(data, status=HTTP_200_OK)
