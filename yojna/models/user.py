from yojna.models.department import DepartmentModel
from yojna.models.sub_department import SubdepartmentModel
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .base import BaseModel
import os
import uuid

from yojna.managers import UserManager


class UserModel(BaseModel, AbstractBaseUser, PermissionsMixin):
    DEPARTMENT_CLERK_1 = "Department clerk 1"
    DEPARTMENT_CLERK_2 = "Department clerk 2"
    DEPARTMENT_ADMIN_HOD = "Department admin hod"
    MASTER_COLLECTOR_DPO = "Master collector dpo"
    COMMON_USER = "User"

    USER_CATEGORY_CHOICE = [
        (DEPARTMENT_CLERK_1 , "Department clerk 1"),
        (DEPARTMENT_CLERK_2 , "Department clerk 2"),
        (DEPARTMENT_ADMIN_HOD , "Department admin hod"),
        (MASTER_COLLECTOR_DPO , "Master collector dpo"),
        (COMMON_USER , "User")
    ]
    name = models.CharField(max_length=64, default=None, null=True, blank=True)
    email = models.EmailField(default=None, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    is_superuser = models.BooleanField(default=False, null=False, blank=False)
    mobile_number = PhoneNumberField(unique=True, blank=True)
    adhaar_no = models.CharField(max_length=100, null=True, blank=True)
    Gender = models.CharField(max_length=6,default=None,null=True,blank=True)
    profile_pic = models.ImageField(upload_to= 'images/', null=True,blank=True,default=None)
    caste = models.CharField(max_length=5,default=None,null=True,blank=True)
    mobile_number_verified_at = models.DateTimeField(default=None, null=True, blank=True)
    bpl = models.CharField(default=None,null=True,blank=True,max_length=15)
    bpl_dharak = models.CharField(default=None,null=True,blank=True,max_length=30)
    role = models.CharField(choices=USER_CATEGORY_CHOICE,default=USER_CATEGORY_CHOICE[4],max_length=100,blank=True,null=True)
    department = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE,default=None,null=True,blank=True)
    subdepartment = models.ForeignKey(SubdepartmentModel,on_delete=models.CASCADE,default=None,null=True,blank=True)
    country = models.CharField(max_length=300,default=None,null=True,blank=True)
    state = models.CharField(max_length=300,default=None,null=True,blank=True)
    city = models.CharField(max_length=300,default=None,null=True,blank=True)
    address = models.TextField(default=None,blank=True,null=True)
    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        ordering = ['name']
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def is_staff(self):
        """

        :return: True, if user is superuser else False
        """
        return self.is_superuser
    def __str__(self):
        return "{a}".format(a=self.name)
        
class User_documents(models.Model):
    user= models.ForeignKey(UserModel, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=100)
    document = models.FileField(upload_to='media')

    class Meta:
        ordering = ['user']
        db_table = 'user_document'
        verbose_name = 'User_Document'
        verbose_name_plural = 'User_Documents'
