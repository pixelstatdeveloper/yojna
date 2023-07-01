from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class hami_yojna(models.Model):
    karyalay1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    mobile_number = PhoneNumberField( blank=True)
    form_date = models.DateField(default=None,null=True,blank=True)
    karyalay2 = models.CharField(max_length=1000,null=True, blank=True, default=None)
    yoj_name= models.CharField(max_length=100,null=True, blank=True, default=None)
    name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    gender = models.CharField(default=None,null=True,blank=True,max_length=100)
    birth_date = models.DateField(default=None,null=True,blank=True)
    jat =  models.CharField(max_length=100, null=True, blank=True)
    mu_post =  models.CharField(max_length=100, null=True, blank=True)
    taluka =  models.CharField(max_length=100, null=True, blank=True)
    jilha =  models.CharField(max_length=100, null=True, blank=True)
    mobile_number1 = PhoneNumberField( blank=True)
    adhaar_no = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=1000, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    khate_kr = models.CharField(max_length=100, null=True, blank=True)
    shakha = models.CharField(max_length=100, null=True, blank=True)
    ifsc = models.CharField(max_length=1000, null=True, blank=True)
    jamin_prakar =  models.CharField(max_length=100, null=True, blank=True)
    gat_kr =  models.CharField(max_length=100, null=True, blank=True)
    kshetra =  models.CharField(max_length=100, null=True, blank=True)
    pike= models.CharField(max_length=1000,null=True, blank=True, default=None)
    tuti_kshetra =  models.CharField(max_length=100, null=True, blank=True)
    sinchan =  models.CharField(max_length=100, null=True, blank=True)
    sinchan_kalavadhi =  models.CharField(max_length=100, null=True, blank=True)
    vij_jodni = models.BooleanField(default=None,null=True,blank=True)
    gruh_vyavstha = models.BooleanField(default=None,null=True,blank=True)
    majur = models.BooleanField(default=None,null=True,blank=True)
    shetkari_varg =  models.CharField(max_length=100, null=True, blank=True)
    daridrya = models.BooleanField(default=None,null=True,blank=True)
    bplkard =  models.CharField(max_length=100, null=True, blank=True)
    nondani_fee = models.BooleanField(default=None,null=True,blank=True)
    shri =  models.CharField(max_length=100, null=True, blank=True)
    padnam =  models.CharField(max_length=100, null=True, blank=True)
    karyalay3 = models.CharField(max_length=1000,null=True, blank=True, default=None)
    shetkari_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "hami_yojna"
        

