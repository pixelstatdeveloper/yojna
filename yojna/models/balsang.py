from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class balsangopan(models.Model):
    name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    age =  models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(default=None,null=True,blank=True)
    education = models.CharField(max_length=1000, null=True, blank=True)
    palak_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    patta = models.CharField(max_length=1000, null=True, blank=True)
    palak_name1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    patta1 = models.CharField(max_length=1000, null=True, blank=True)
    nate =  models.CharField(max_length=100, null=True, blank=True)
    income =  models.CharField(max_length=100, null=True, blank=True)
    buisness = models.CharField(max_length=1000, null=True, blank=True)
    aai = models.BooleanField(default=None,null=True,blank=True)
    vadil = models.BooleanField(default=None,null=True,blank=True)
    mahiti =  models.CharField(max_length=100, null=True, blank=True)
    sthiti =  models.CharField(max_length=100, null=True, blank=True)
    bhau =  models.CharField(max_length=100, null=True, blank=True)
    bahin =  models.CharField(max_length=100, null=True, blank=True)
    aaji =  models.CharField(max_length=100, null=True, blank=True)
    name1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    patta2 = models.CharField(max_length=1000, null=True, blank=True)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "balsangopan"
        

