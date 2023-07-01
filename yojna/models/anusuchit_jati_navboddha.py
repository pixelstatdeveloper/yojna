from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class ramai_gharkul(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=1000,default=None,null=True,blank=True)
    fa_name = models.CharField(max_length=1000,default=None,null=True,blank=True)
    cu_address = models.TextField(default=None,null=True,blank=True)
    ghar_address = models.TextField(default=None,null=True,blank=True)
    pe_address = models.TextField(default=None,null=True,blank=True)
    kshetrafal = models.CharField(default=None,null=True,blank=True,max_length=100)
    birth_date = models.DateField(default=None,null=True,blank=True)
    age = models.IntegerField(default=None,null=True,blank=True)
    birth_place = models.CharField(max_length=1000,default=None,null=True,blank=True)
    caste = models.CharField(default=None,null=True,blank=True,max_length=200)
    education = models.CharField(default=None,null=True,blank=True,max_length=400)
    business = models.CharField(default=None,null=True,blank=True,max_length=500)
    ration_no = models.CharField(default=None,null=True,blank=True,max_length=200)
    fa_business = models.CharField(default=None,null=True,blank=True,max_length=500)
    income = models.BigIntegerField(default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media',default=None,null=True,blank=True)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    apply_date = models.DateField(default=None,null=True,blank=True)
    name_1 = models.CharField(max_length=1000,default=None,null=True,blank=True)
    pradhanya = models.CharField(max_length=1000,default=None,null=True,blank=True)
  
    class Meta:
        db_table = "Ramai_Gharkul"
    def __str__(self) -> str:
        return str(self.name)