from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class aarogya_patrika(models.Model):
    namuna= models.CharField(max_length=100,null=True, blank=True, default=None)
    namuna_tarikh = models.DateField(default=None,null=True,blank=True)
    shetkari_name= models.CharField(max_length=100,null=True, blank=True, default=None)
    mobile_number = PhoneNumberField( blank=True)
    mrud_namuna = models.CharField(max_length=100,default=None,null=True,blank=True)
    gav= models.CharField(max_length=100,null=True, blank=True, default=None)
    post= models.CharField(max_length=100,null=True, blank=True, default=None)
    taluka= models.CharField(max_length=100,null=True, blank=True, default=None)
    jilha= models.CharField(max_length=100,null=True, blank=True, default=None)
    sarve= models.CharField(max_length=100,null=True, blank=True, default=None)
    jamin_utara = models.CharField(max_length=100,default=None,null=True,blank=True)
    panyacha = models.CharField(max_length=100,default=None,null=True,blank=True)
    lakshne= models.CharField(max_length=100,null=True, blank=True, default=None)
    jamin_kholi = models.CharField(max_length=100,default=None,null=True,blank=True)
    pik1 = models.CharField(max_length=100,default=None,null=True,blank=True)
    pik2 = models.CharField(max_length=100,default=None,null=True,blank=True)
    korad = models.CharField(max_length=100,default=None,null=True,blank=True)
    kshetra = models.CharField(max_length=100,default=None,null=True,blank=True)
    hangam_pik = models.CharField(max_length=100,default=None,null=True,blank=True)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    name1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "aarogya_patrika"
        

