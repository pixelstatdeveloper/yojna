from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class otsp_shivnyantra(models.Model):
    name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    sam_patta = models.CharField(max_length=1000, null=True, blank=True)
    mukkam = models.CharField(max_length=1000, null=True, blank=True)
    post= models.CharField(max_length=1000,null=True, blank=True, default=None)
    taluka= models.CharField(max_length=1000,null=True, blank=True, default=None)
    birth_date = models.DateField(default=None,null=True,blank=True)
    tc = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    jati = models.BooleanField(default=None,null=True,blank=True)
    dakhla = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    jat =  models.CharField(max_length=100, null=True, blank=True)
    potjat =  models.CharField(max_length=100, null=True, blank=True)
    vivahit =  models.CharField(max_length=100, null=True, blank=True)
    patiname= models.CharField(max_length=1000,null=True, blank=True, default=None)
    buisness = models.CharField(max_length=1000, null=True, blank=True)
    income =  models.CharField(max_length=100, null=True, blank=True)
    fa_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    buisness1 = models.CharField(max_length=1000, null=True, blank=True)
    income1 =  models.CharField(max_length=100, null=True, blank=True)
    income2 =  models.CharField(max_length=100, null=True, blank=True)
    dakhla1 = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    buisness2 = models.CharField(max_length=1000, null=True, blank=True)
    income3 =  models.CharField(max_length=100, null=True, blank=True)
    prashikshan= models.CharField(max_length=1000,null=True, blank=True, default=None)
    pramanpatra = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    prashikshan1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    pramanpatra2 = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    sthal =  models.CharField(max_length=100, null=True, blank=True)
    form_date = models.DateField(default=None,null=True,blank=True)
    patta = models.CharField(max_length=1000, null=True, blank=True)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "otsp_shivnyantra"
        

