from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class gayakvad(models.Model):
    name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    jilha_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    adhi1_date = models.DateField(default=None,null=True,blank=True)
    adhi2_date = models.DateField(default=None,null=True,blank=True)
    adhi1 =  models.CharField(max_length=100, null=True, blank=True)
    adhi2 =  models.CharField(max_length=100, null=True, blank=True)
    mobile_number = PhoneNumberField( blank=True)
    paripurn_patta = models.CharField(max_length=1000, null=True, blank=True)
    sambandhit = models.CharField(max_length=1000, null=True, blank=True)
    upvidhi = models.CharField(max_length=1000, null=True, blank=True)
    padadhi1_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    padadhi2_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    mob1 = PhoneNumberField( blank=True)
    mob2 = PhoneNumberField( blank=True)
    arj_pur= models.CharField(max_length=1000,null=True, blank=True, default=None)
    anubhav =  models.CharField(max_length=100, null=True, blank=True)
    lekha_pari= models.CharField(max_length=1000,null=True, blank=True, default=None)
    varshik_aha= models.CharField(max_length=1000,null=True, blank=True, default=None)
    swatantra_lekha= models.CharField(max_length=1000,null=True, blank=True, default=None)
    sambandhit_sanstha= models.CharField(max_length=1000,null=True, blank=True, default=None)
    upkram= models.CharField(max_length=1000,null=True, blank=True, default=None)
    vyaktigat= models.CharField(max_length=1000,null=True, blank=True, default=None)
    sadar_sansthes= models.CharField(max_length=1000,null=True, blank=True, default=None)
    vaishishtya= models.CharField(max_length=1000,null=True, blank=True, default=None)
    vaishishtya1 = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    dakhla= models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    name2= models.CharField(max_length=1000,null=True, blank=True, default=None)
    pari_name1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    pari_name2= models.CharField(max_length=1000,null=True, blank=True, default=None)
    pari_name3= models.CharField(max_length=1000,null=True, blank=True, default=None)
    from1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    from2= models.CharField(max_length=1000,null=True, blank=True, default=None)
    from3= models.CharField(max_length=1000,null=True, blank=True, default=None)
    pari_date1 = models.DateField(default=None,null=True,blank=True)
    pari_date2 = models.DateField(default=None,null=True,blank=True)
    pari_date3 = models.DateField(default=None,null=True,blank=True)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = "gayakvad"
        

