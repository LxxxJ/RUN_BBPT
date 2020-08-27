from django.db import models
import time

# Create your models here.

class UserInfo(models.Model):
    user_type_choices=(
        (1,"Common"),
        (2,"Admini")
    )
    nid = models.AutoField(primary_key=True)
    user_type = models.IntegerField(choices=user_type_choices)
    user_name = models.CharField(max_length=32,unique=True,null=False)
    password = models.CharField(max_length=32,null=False)
    rank = models.IntegerField()
    total_mile = models.FloatField(default=0.0)
    created_time = models.DateTimeField(auto_now = True)
    updated_time = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.user_name

class UserToken(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
    created_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.user_name

class GroupInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=32,unique=True,null=False)
    cap = models.ForeignKey(UserInfo,on_delete=models.CASCADE,related_name='cap_id')
    group_number = models.IntegerField()
    group_intro = models.CharField(max_length=1000,null=True)
    created_time = models.DateTimeField(auto_now = True)
    updated_time = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.group_name

class GroupMember(models.Model):
    nid = models.AutoField(primary_key=True)
    group_id = models.IntegerField()
    user_id = models.ForeignKey(UserInfo,on_delete=models.CASCADE,related_name='user')
    join_time = models.DateTimeField(auto_now = True)

class RunInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    run_mile = models.FloatField()
    run_time = models.DateTimeField()
    created_time = models.DateTimeField(auto_now = True)

class RankInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    image = models.BinaryField()
    rank = models.IntegerField()
    applied_by = models.IntegerField()
    is_checked = models.IntegerField(default=0)
    checked_by = models.IntegerField()
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=True)