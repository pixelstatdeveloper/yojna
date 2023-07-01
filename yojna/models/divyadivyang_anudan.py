from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class divyadivyang_anudan(models.Model):
    husband_name = models.CharField(max_length=100,default=None,null=True,blank=True)
    wife_name = models.CharField(max_length=100,default=None,null=True,blank=True)
    husband_birth = models.DateField(default=None,null=True,blank=True)
    wife_birth = models.DateField(default=None,null=True,blank=True)
    husband_age = models.IntegerField(default=None,null=True,blank=True)
    wife_age = models.IntegerField(default=None,null=True,blank=True)
    husband_gender = models.CharField(max_length=15,default=None,null=True,blank=True)
    wife_gender = models.CharField(max_length=15,default=None,null=True,blank=True)
    husband_caste = models.CharField(default=None,null=True,blank=True,max_length=15)
    wife_caste = models.CharField(default=None,null=True,blank=True,max_length=15)
    husband_edu = models.CharField(default=None,null=True,blank=True,max_length=80)
    wife_edu = models.CharField(default=None,null=True,blank=True,max_length=80)
    income = models.CharField(default=None,null=True,blank=True,max_length=50)
    vivah_date = models.DateField(default=None,null=True,blank=True)
    husdivyang_type = models.CharField(default=None,null=True,blank=True,max_length=70)
    hus_percent = models.FloatField(default=None,null=True,blank=True)
    wifedivyang_type = models.CharField(default=None,null=True,blank=True,max_length=70)
    wife_percent = models.FloatField(default=None,null=True,blank=True)
    hus_certificateno = models.CharField(default=None,null=True,blank=True,max_length=30)
    huscertificate_date = models.DateField(default=None,null=True,blank=True)
    wife_certificateno = models.CharField(default=None,null=True,blank=True,max_length=30)
    wifecertificate_date = models.DateField(default=None,null=True,blank=True)
    hus_vyavsay = models.CharField(default=None,null=True,blank=True,max_length=80)
    wife_vyavsay = models.CharField(default=None,null=True,blank=True,max_length=80)
    husadhar_no = models.IntegerField(default=None,null=True,blank=True)
    wifeadhar_no = models.IntegerField(default=None,null=True,blank=True)
    hus_address = models.CharField(default=None,null=True,blank=True,max_length=200)
    wifemaher_address = models.CharField(default=None,null=True,blank=True,max_length=200)
    mobile_no1 = PhoneNumberField(unique=True, blank=True)
    mobile_no2 = PhoneNumberField(unique=True, blank=True)
    yojna_name = models.CharField(default=None,null=True,blank=True,max_length=100)
    benefit = models.CharField(default=None,null=True,blank=True,max_length=20)
    hus_photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    wife_photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    hus_sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    wife_sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)    
    
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = "divyadivyang_anudan"
    def __str__(self) -> str:
        return str(self.husband_name)