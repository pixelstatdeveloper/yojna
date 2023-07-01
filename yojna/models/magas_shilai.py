from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class magas_shilai(models.Model):
    name = models.CharField(max_length=100,default=None,null=True,blank=True)
    address = models.CharField(default=None,null=True,blank=True,max_length=200)
    panchayat_prabhag = models.CharField(default=None,null=True,blank=True,max_length=80)
    zp_prabhag = models.CharField(default=None,null=True,blank=True,max_length=80)
    yojna_name = models.CharField(default=None,null=True,blank=True,max_length=100)
    jat = models.CharField(default=None,null=True,blank=True,max_length=50)
    caste = models.CharField(default=None,null=True,blank=True,max_length=20)
    birthdate = models.DateField(default=None,null=True,blank=True)
    education = models.CharField(default=None,null=True,blank=True,max_length=100)
    san = models.IntegerField(null=True, blank=True, default=None)
    income = models.CharField(default=None,null=True,blank=True,max_length=50)
    daridray = models.CharField(default=None,null=True,blank=True,max_length=15)
    kutumb_no = models.CharField(default=None,null=True,blank=True,max_length=25)
    sheti = models.CharField(default=None,null=True,blank=True,max_length=15)
    taluka = models.CharField(default=None,null=True,blank=True,max_length=25)
    gav = models.CharField(default=None,null=True,blank=True,max_length=25)
    shetrafal = models.CharField(default=None,null=True,blank=True,max_length=60)
    adhar_no = models.IntegerField(default=None,null=True,blank=True)
    bank = models.CharField(default=None,null=True,blank=True,max_length=120)
    thikan = models.CharField(default=None,null=True,blank=True,max_length=25)
    dinank = models.DateField(default=None,null=True,blank=True)
    purn_nav = models.CharField(max_length=100,default=None,null=True,blank=True)
    patta = models.CharField(default=None,null=True,blank=True,max_length=120)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)    
    
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = "magas_shilai"
    def __str__(self) -> str:
        return str(self.name)