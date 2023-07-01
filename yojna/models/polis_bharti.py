from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class polis_bhartipurva(models.Model):
    name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    fa_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    mobile_number = PhoneNumberField( blank=True)
    paripurn_patta = models.CharField(max_length=1000, null=True, blank=True)
    dharma = models.CharField(max_length=100, null=True, blank=True)
    dharma_dakhla = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    jat = models.CharField(max_length=100, null=True, blank=True)
    varshik_utpanna = models.CharField(max_length=100, null=True, blank=True)
    dakhla = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    rahivasi = models.CharField(max_length=50, null=True, blank=True)
    rahi_dakhla = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    hsc = models.CharField(max_length=100, null=True, blank=True)
    hsc_dakhla = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    unchi = models.CharField(max_length=100, null=True, blank=True)
    chhati = models.CharField(max_length=100, null=True, blank=True)
    fugvun = models.CharField(max_length=100, null=True, blank=True)
    seva_kard = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(default=None,null=True,blank=True)
    birth_date1 = models.DateField(default=None,null=True,blank=True)
    varsh = models.CharField(max_length=100, null=True, blank=True)
    mahina = models.CharField(max_length=100, null=True, blank=True)
    divas = models.CharField(max_length=100, null=True, blank=True)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    name1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    form_date = models.DateField(default=None,null=True,blank=True)
    mobile_number1 = PhoneNumberField( blank=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "polis_bhartipurva"
        

