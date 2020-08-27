from rest_framework import serializers
from .models import *

class GroupInfoModelSerializer(serializers.ModelSerializer):
    cap_name = serializers.CharField(source='cap.user_name')
    class Meta:
        model = GroupInfo
        fields = ('group_name','cap_name','group_intro','group_number')

class GroupMemberModelSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user_id.user_name')
    user_rank = serializers.IntegerField(source='user_id.rank')
    user_mile = serializers.FloatField(source='user_id.total_mile')
    class Meta:
        model = GroupMember
        fields = ('group_id','user_name','user_rank','user_mile')

class UserInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields=('user_name','rank','total_mile','nid')

class RunInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunInfo
        fields = ('run_mile','run_time')

class GroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupInfo
        fields=('nid',)

class GroupUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields=('group_id',)

class CreateGroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupInfo
        fields = ('nid',)

class RankInfoModelSerializer(serializers.ModelSerializer):
    image = serializers.CharField()
    class Meta:
        model = RankInfo
        fields = ('nid','rank','is_checked','applied_by','image')

class UserTokenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = ('token',)



