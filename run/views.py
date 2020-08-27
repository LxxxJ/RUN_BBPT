from django.http import HttpResponse,JsonResponse
from .Serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .utils.auth import VIP
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework import exceptions

# Create your views here.

def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m=hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()

@method_decorator(csrf_exempt)
def login(request):
    if request.method == "GET":
        name = request.GET.get('username')
        password = request.GET.get('password')
        try:
            user = UserInfo.objects.get(user_name=name)
        except ObjectDoesNotExist:
            return HttpResponse("用户不存在")
        else:
            if user.password == password:
                token = md5(name)
                UserToken.objects.update_or_create(user_id=user.nid,defaults={'token':token})
                return HttpResponse("登录成功")
            else:
                return HttpResponse("登录失败")

@method_decorator(csrf_exempt)
def signup(request):
    if request.method == "POST":
        name = request.POST.get('username',None)
        password = request.POST.get('password',None)
        try:
            UserInfo.objects.get(user_name=name)
        except ObjectDoesNotExist:
            UserInfo.objects.create(user_name=name, password=password)
            return HttpResponse("注册成功")
        else:
            return HttpResponse("用户名已存在")

class UserInfoAPIView(APIView):
    permission_classes = []
    def get(self, request, format=None):
        UserName = self.request.query_params.get("userName",0)
        developer=UserInfo.objects.filter(user_name=UserName)
        if developer:
            userInfo = UserInfoModelSerializer(developer, many=True)
            return Response(userInfo.data)
        else:
            return Response("查无此人")

class UserInfoAPIView2(APIView):
    permission_classes = []
    def get(self, request, format=None):
        UserID = self.request.query_params.get("userid",0)
        developer=UserInfo.objects.filter(nid=UserID)
        if developer:
            userInfo = UserInfoModelSerializer(developer, many=True)
            return Response(userInfo.data)
        else:
            return Response("查无此人")

class GroupInfoAPIView(APIView):
    permission_classes = []
    def get(self, request, format=None):
        group=GroupInfo.objects.all()
        if group:
            groupInfo = GroupInfoModelSerializer(group, many=True)
            return Response(groupInfo.data)
        else:
            return Response("查无此群")


class CreateGroupView(APIView):
    permission_classes = []
    def get(self,request,format=None):
        id = self.request.query_params.get("userid",0)
        groupName = self.request.query_params.get("groupName",0)
        groupIntro = self.request.query_params.get("groupIntro",0)
        user = UserInfo.objects.filter(nid=id)
        if user:
            if GroupInfo.objects.filter(group_name=groupName).count() == 0:
                GroupInfo.objects.create(group_name=groupName, cap_id=id, group_intro=groupIntro, group_number=0)
                group = GroupInfo.objects.filter(group_name=groupName)
                groupInfo = CreateGroupModelSerializer(group,many=True)
                return Response(groupInfo.data)
            else:
                return Response("创建失败")
        else:
            return Response("账号出现问题")


@method_decorator(csrf_exempt)
def createGroup(request):
    if request.method == "POST":
        id = int(request.POST.get('userid',None))
        groupName = request.POST.get('groupName',None)
        groupIntro = request.POST.get('groupIntro',None)
        user = UserInfo.objects.filter(nid=id)
        if user:
            if GroupInfo.objects.filter(group_name=groupName).count() == 0:
                GroupInfo.objects.create(group_name=groupName,cap_id=id,group_intro=groupIntro,group_number=0)
                id = GroupInfo.objects.get(group_name=groupName).nid
                return HttpResponse(id)
            else:
                return HttpResponse("创建失败")
        else:
            return HttpResponse("账号出现问题")


@method_decorator(csrf_exempt)
def haveGroup(request):
    if request.method == "GET":
        id = request.GET.get('userid',None)
        if GroupMember.objects.filter(user_id=id).count() == 0:
            return HttpResponse("没有团队")
        else:
            return HttpResponse("有团队")


@method_decorator(csrf_exempt)
def joinGroup(request):
    if request.method == "POST":
        userid = request.POST.get('userid',None)
        groupid = int(request.POST.get('groupid',None))
        GroupMember.objects.create(group_id=groupid,user_id_id=userid)
        num = GroupMember.objects.filter(group_id=groupid).count() + 1
        GroupInfo.objects.filter(nid=groupid).update(group_number=num)
        return HttpResponse("加入成功")

@method_decorator(csrf_exempt)
def exitGroup(request):
    if request.method == "POST":
        userid = request.POST.get('userid',None)
        groupid = int(request.POST.get('groupid',None))
        GroupMember.objects.filter(user_id=userid).delete()
        num = GroupMember.objects.filter(group_id=groupid).count() - 1
        GroupInfo.objects.filter(nid=groupid).update(group_number = num)
        return HttpResponse("删除成功")

class GroupMemberAPIView(APIView):
    permission_classes = []
    def get(self, request, format=None):
        groupId = self.request.query_params.get("groupId",0)
        developer=GroupMember.objects.filter(group_id=groupId).order_by('-user_id__rank')
        if developer:
            userInfo = GroupMemberModelSerializer(developer, many=True)
            return Response(userInfo.data)
        else:
            return Response("查无此人")

class RunInfoAPIView(APIView):
    permission_classes = []
    def get(self,request,format=None):
        userID = self.request.query_params.get("userID",0)
        developer = RunInfo.objects.filter(user_id=userID)
        if developer:
            runInfo = RunInfoModelSerializer(developer,many=True)
            return Response(runInfo.data)
        else:
            return Response("查无此人")


class GroupAPIView(APIView):
    permission_classes = []
    def get(self, request, format=None):
        groupname = self.request.query_params.get("groupName", 0)
        group = GroupInfo.objects.filter(group_name=groupname)
        if group:
            groupID = GroupModelSerializer(group, many=True)
            return Response(groupID.data)
        else:
            return Response("跑团不存在")

class GroupUserAPIView(APIView):
    permission_classes = []
    def get(self, request, format=None):
        userid = self.request.query_params.get("userID", 0)
        user = GroupMember.objects.filter(user_id=userid)
        if user:
            groupID = GroupUserModelSerializer(user, many=True)
            return Response(groupID.data)
        else:
            return Response("用户没有跑团")

class VIPRankView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [VIP,]
    def get(self,request):
        rankInfo = RankInfo.objects.all()
        re = RankInfoModelSerializer(rankInfo,many=True)
        return Response(re.data)

class UserTokenAPIView(APIView):
    permission_classes = []
    def get(self,request,format=None):
        userid = self.request.query_params.get("userid",0)
        usertoken = UserToken.objects.filter(user=userid)
        if usertoken:
            token = UserTokenModelSerializer(usertoken,many=True)
            return Response(token.data)
        else:
            return Response("用户没有认证")

def GetApplication(request):
    if request.method == "POST":
        user_id = int(request.POST.get('userid'))
        rank = int(request.POST.get('rank'))
        image = int(request.data.get('image',None))
        RankInfo.objects.create(image=image,rank=rank,applied_by=user_id,is_checked=0,checked_by=0)
        return HttpResponse("申请成功")

@method_decorator(csrf_exempt)
def CheckApplication(request):
    if request.method == "POST":
        username = request.POST.get('username')
        apply_id = request.POST.get('nid')
        user_id = UserInfo.objects.get(user_name=username).nid
        RankInfo.objects.filter(nid=apply_id).update(is_checked=1,checked_by=user_id)
        rank = RankInfo.objects.get(nid=apply_id).rank
        user = RankInfo.objects.get(nid=apply_id).applied_by
        new_rank = UserInfo.objects.get(nid=user).rank + rank
        UserInfo.objects.filter(nid=user).update(rank=new_rank)
        return HttpResponse("确认成功")

@method_decorator(csrf_exempt)
def MileApplication(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        mile = request.POST.get('mile')










