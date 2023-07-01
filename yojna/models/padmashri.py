from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class karmavir(models.Model):
    name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    jilha_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    mobile_number = PhoneNumberField( blank=True)
    paripurn_patta = models.CharField(max_length=1000, null=True, blank=True)
    birth_date = models.DateField(default=None,null=True,blank=True)
    purava = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    age = models.IntegerField(default=None,null=True,blank=True)
    education = models.CharField(max_length=1000, null=True, blank=True)
    business = models.CharField(default=None,null=True,blank=True,max_length=1000)
    jat =  models.CharField(max_length=100, null=True, blank=True)
    pramanpatra = models.CharField(max_length=100, null=True, blank=True)
    hudda = models.CharField(max_length=100, null=True, blank=True)
    thikan = models.CharField(max_length=100, null=True, blank=True)
    patni_hyat= models.CharField(max_length=1000,null=True, blank=True, default=None)
    samajik= models.CharField(max_length=100,null=True, blank=True, default=None)
    arj_pur = models.CharField(default=None,null=True,blank=True,max_length=500)
    anujati= models.CharField(max_length=1000,null=True, blank=True, default=None)
    vyakti_sahitya= models.CharField(max_length=1000,null=True, blank=True, default=None)
    jya_sanstha = models.CharField(default=None,null=True,blank=True,max_length=500)
    samkaly_kshetra = models.CharField(default=None,null=True,blank=True,max_length=500)
    karyakartya = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    yapurvi_bahu = models.CharField(default=None,null=True,blank=True,max_length=500)
    karkarta_sadhya = models.CharField(default=None,null=True,blank=True,max_length=500)
    vidhanmandal = models.CharField(default=None,null=True,blank=True,max_length=500)
    vyakti_karyakarta = models.CharField(default=None,null=True,blank=True,max_length=500)
    vyakti_karyakarta1 = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    shifaras = models.CharField(default=None,null=True,blank=True,max_length=500)
    itar = models.CharField(default=None,null=True,blank=True,max_length=500)
    form_date = models.DateField(default=None,null=True,blank=True)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "karmavir"
        

