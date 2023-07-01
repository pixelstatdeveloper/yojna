from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class sanstha_sabhasad(models.Model):
    sansname =  models.CharField(max_length=1000, null=True, blank=True)
    form_date = models.DateField(default=None,null=True,blank=True)
    name3= models.CharField(max_length=1000,null=True, blank=True, default=None)
    form_date1 = models.DateField(default=None,null=True,blank=True)
    singh = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    sansthaname= models.CharField(max_length=1000,null=True, blank=True, default=None)
    patta =  models.CharField(max_length=1000, null=True, blank=True)
    non_kr = models.CharField(max_length=100, null=True, blank=True)
    satyaprat = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    sachivname1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    patta2 =  models.CharField(max_length=1000, null=True, blank=True)
    granth_sankhya = models.CharField(max_length=100, null=True, blank=True)
    sabh_sankhya = models.CharField(max_length=100, null=True, blank=True)
    devghevi = models.CharField(max_length=100, null=True, blank=True)
    tharav_kr = models.CharField(max_length=100, null=True, blank=True)
    tharav_date = models.DateField(default=None,null=True,blank=True)
    satyaprat1 = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    karya_sadasya1 = models.CharField(max_length=100, null=True, blank=True)
    karya_sadasya2 = models.CharField(max_length=100, null=True, blank=True)
    karya_sadasya3 = models.CharField(max_length=100, null=True, blank=True)
    karya_sadasya4 = models.CharField(max_length=100, null=True, blank=True)
    karya_sadasya5 = models.CharField(max_length=100, null=True, blank=True)
    karya_sadasya6 = models.CharField(max_length=100, null=True, blank=True)
    karya_sadasya7 = models.CharField(max_length=100, null=True, blank=True)
    itar =  models.CharField(max_length=1000, null=True, blank=True)
    shri =  models.CharField(max_length=1000, null=True, blank=True)
    shikka = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "sanstha_sabhasad"
        

