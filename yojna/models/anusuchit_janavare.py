from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class anusuchit_janavare(models.Model):
    name = models.CharField(max_length=100,default=None,null=True,blank=True)
    photo_id = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    mukampost = models.CharField(max_length=40,default=None,null=True,blank=True)
    taluka = models.CharField(max_length=40,default=None,null=True,blank=True)
    pincode = models.IntegerField(default=None,null=True,blank=True)
    mobile_no = PhoneNumberField(unique=True, blank=True)
    age_year = models.IntegerField(default=None,null=True,blank=True)
    gender = models.CharField(max_length=10,default=None,null=True,blank=True)
    daridrya_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    shetjamin_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    sankarit_gayi = models.CharField(max_length=4,default=None,null=True,blank=True)
    gavthi_gayi = models.CharField(max_length=4,default=None,null=True,blank=True)
    sheti_bail = models.CharField(max_length=4,default=None,null=True,blank=True)
    murha_mhais = models.CharField(max_length=4,default=None,null=True,blank=True)
    gotha_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    kiti_janavar = models.CharField(max_length=4,default=None,null=True,blank=True)
    dughdautpadan_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    dughdautpadan_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    anuadi_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    anuadi_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    bachatgat_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    bachatgat_name = models.CharField(max_length=80,default=None,null=True,blank=True)
    bachatgat_address = models.CharField(max_length=100,default=None,null=True,blank=True)
    bachatgat_shetra = models.CharField(max_length=100,default=None,null=True,blank=True)
    berozgar_yn = models.CharField(max_length=8,default=None,null=True,blank=True)
    sevayojna_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    bank_name = models.CharField(max_length=70,default=None,null=True,blank=True)
    bank_branch = models.CharField(max_length=40,default=None,null=True,blank=True)
    sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)

    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "anusuchit_janavare"
    def __str__(self) -> str:
        return str(self.name)