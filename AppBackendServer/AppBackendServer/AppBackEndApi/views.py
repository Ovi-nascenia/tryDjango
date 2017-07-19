from django.shortcuts import render
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PromotionAd
from .serializers import PromotionSerializer
from rest_framework.request import Request

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your views here.



class PromotionList(APIView):
    
    
    def get(self,Request,token):

     #   token = Token.objects.create(user=settings.AUTH_USER_MODEL)
        #user_with_token = Token.objects.get(Token=token)
        is_tokened = Token.objects.filter(Token=token).exist()
        print(is_tokened)
        promotion = PromotionAd.objects.all()
        serializer = PromotionSerializer(promotion, many = True)
        return Response(serializer.data)
        pass
    def post(self):
        pass
    
