from ..models import *
from rest_framework import exceptions
from django.http import HttpResponse
class Authentication(object):
    def authenticate(self,request):
        token = request._request.GET.get('token')
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (token_obj.user_id,token_obj)

    def authenticate_header(self,request):
        pass

class VIP(object):
    def has_permission(self,request,view):
        token = request._request.GET.get('token')
        user_id = UserToken.objects.filter(token=token).first().user_id
        user_type = UserInfo.objects.get(nid=user_id).user_type
        if user_type < 2:
            return False
        return True