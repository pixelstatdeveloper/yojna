from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class adivasividyarthi_engraji(models.Model):
    std1 = models.CharField(max_length=2,default=None,null=True,blank=True)
    std2 = models.CharField(max_length=2,default=None,null=True,blank=True)
    name = models.CharField(max_length=80,default=None,null=True,blank=True)
    birth_date = models.DateField(default=None,null=True,blank=True)
    birth_place = models.CharField(max_length=30,default=None,null=True,blank=True)
    jamat = models.CharField(max_length=60,default=None,null=True,blank=True)
    nation = models.CharField(max_length=25,default=None,null=True,blank=True)
    rahivasi_yn = models.CharField(max_length=4,default=None,null=True,blank=True) 
    rahivasi = models.CharField(max_length=30,default=None,null=True,blank=True)
    father_name = models.CharField(max_length=80,default=None,null=True,blank=True)
    current_add = models.CharField(max_length=120,default=None,null=True,blank=True)
    kayam_add = models.CharField(max_length=120,default=None,null=True,blank=True)
    mobile1 = PhoneNumberField(unique=True, blank=True)
    mobile2 = PhoneNumberField(unique=True, blank=True)
    mother_name = models.CharField(max_length=80,default=None,null=True,blank=True)
    income_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    vyavsay = models.CharField(max_length=40,default=None,null=True,blank=True)
    nokardar_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    daridrya_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    mahilapalak_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)

    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "adivasividyarthi_engraji"
    def __str__(self) -> str:
        return str(self.name)