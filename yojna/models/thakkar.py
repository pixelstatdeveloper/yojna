from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel


class thakkar(models.Model):
    san = models.CharField(max_length=1000,null=True, blank=True, default=None)
    gp_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    tbarea_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    paripurn_patta = models.CharField(max_length=1000, null=True, blank=True)
    total_population = models.IntegerField(null=True, blank=True, default=None)
    anusuchit_population = models.IntegerField(null=True, blank=True, default=None)
    living_castes = models.CharField(max_length=1000,null=True, blank=True, default=None)
    prastav_bandhkam = models.CharField(max_length=3000,null=True, blank=True, default=None)
    bfor_anudan = models.CharField(max_length=100,null=True, blank=True, default=None)
    anudan_amount = models.CharField(max_length=100,null=True, blank=True, default=None)
    gp_xtranudan = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    gp_sixmonth = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    talathi_satbara = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    gp_shilak = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    sachivsign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    sarpanchsign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "thakkar"
        

