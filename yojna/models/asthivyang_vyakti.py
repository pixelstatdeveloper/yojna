from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class asthivyang_vyakti(models.Model):
    name = models.CharField(max_length=200,default=None,null=True,blank=True)
    birth_date = models.DateField(default=None,null=True,blank=True)
    birthdate_age = models.CharField(max_length=100,default=None,null=True,blank=True)
    gender = models.CharField(default=None,null=True,blank=True,max_length=40)
    caste = models.CharField(default=None,null=True,blank=True,max_length=100)
    education = models.CharField(default=None,null=True,blank=True,max_length=200)
    married = models.CharField(default=None,null=True,blank=True,max_length=60)
    income = models.BigIntegerField(default=None,null=True,blank=True)
    handicap_type = models.CharField(default=None,null=True,blank=True,max_length=200)
    percent = models.FloatField(default=None,null=True,blank=True)
    handicap_certificate_no = models.CharField(default=None,null=True,blank=True,max_length=200)
    form_date = models.DateField(default=None,null=True,blank=True)
    business = models.CharField(default=None,null=True,blank=True,max_length=500)
    adhar_no = models.IntegerField(default=None,null=True,blank=True)
    address = models.CharField(default=None,null=True,blank=True,max_length=500)
    mobile_no = PhoneNumberField(unique=True, blank=True)
    avashak_seva = models.TextField(default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    previous_benefit = models.CharField(default=None,null=True,blank=True,max_length=40)
    
    
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = "asthivyang_vyakti"
    def __str__(self) -> str:
        return str(self.name)