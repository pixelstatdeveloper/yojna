from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class anusuchit_50takke(models.Model):
    name = models.CharField(max_length=100,default=None,null=True,blank=True)
    photo_id = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    mukampost = models.CharField(max_length=40,default=None,null=True,blank=True)
    taluka = models.CharField(max_length=40,default=None,null=True,blank=True)
    pincode = models.IntegerField(default=None,null=True,blank=True)
    mobile_no = PhoneNumberField(unique=True, blank=True)
    age_year = models.IntegerField(default=None,null=True,blank=True)
    age_month = models.IntegerField(default=None,null=True,blank=True)
    gender = models.CharField(max_length=10,default=None,null=True,blank=True)
    daridrya_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    daridry_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    jaga_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    prashikshan_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    anujamat_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    bhumihin_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    bachatgat_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    bachatgat_name = models.CharField(max_length=80,default=None,null=True,blank=True)
    bachatgat_address = models.CharField(max_length=100,default=None,null=True,blank=True)
    bachatgat_shetra = models.CharField(max_length=100,default=None,null=True,blank=True)
    berozgar_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    sevayojna_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    nav = models.CharField(max_length=80,default=None,null=True,blank=True)
    place = models.CharField(max_length=50,default=None,null=True,blank=True)
    dinank = models.DateField(default=None,null=True,blank=True)

    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "anusuchit_50takke"
    def __str__(self) -> str:
        return str(self.name)