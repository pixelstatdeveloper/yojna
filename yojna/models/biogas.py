from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class navin_rashtriy(models.Model):
    samiti= models.CharField(max_length=100,null=True, blank=True, default=None)
    name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    patta = models.CharField(max_length=1000, null=True, blank=True)
    jirayat= models.CharField(max_length=100,null=True, blank=True, default=None)
    bagayat= models.CharField(max_length=100,null=True, blank=True, default=None)
    ekun= models.CharField(max_length=100,null=True, blank=True, default=None)
    mothi= models.CharField(max_length=100,null=True, blank=True, default=None)
    lahan= models.CharField(max_length=100,null=True, blank=True, default=None)
    jan_ekun= models.CharField(max_length=100,null=True, blank=True, default=None)
    sanyantra = models.CharField(max_length=50,null=True, blank=True, default=None)
    sandas = models.CharField(max_length=50,null=True, blank=True, default=None)
    sandas_sankhya= models.CharField(max_length=100,null=True, blank=True, default=None)
    vyakti_mothi= models.CharField(max_length=100,null=True, blank=True, default=None)
    vyakti_lahan= models.CharField(max_length=100,null=True, blank=True, default=None)
    vyakti_ekun= models.CharField(max_length=100,null=True, blank=True, default=None)
    gas_sway = models.CharField(max_length=50,null=True, blank=True, default=None)
    rakkam= models.CharField(max_length=100,null=True, blank=True, default=None)
    shetmajur = models.CharField(max_length=50,null=True, blank=True, default=None)
    ghanmiter= models.CharField(max_length=100,null=True, blank=True, default=None)
    prakar= models.CharField(max_length=100,null=True, blank=True, default=None)
    akar= models.CharField(max_length=100,null=True, blank=True, default=None)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    name1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    patta1 = models.CharField(max_length=1000, null=True, blank=True)
    arj_name1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    he_aar= models.CharField(max_length=100,null=True, blank=True, default=None)
    sankhya= models.CharField(max_length=100,null=True, blank=True, default=None)
    pra_akar= models.CharField(max_length=100,null=True, blank=True, default=None)
    arj_name2= models.CharField(max_length=1000,null=True, blank=True, default=None)
    he_aar2= models.CharField(max_length=100,null=True, blank=True, default=None)
    sankhya2= models.CharField(max_length=100,null=True, blank=True, default=None)
    pra_akar2= models.CharField(max_length=100,null=True, blank=True, default=None)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "navin_rashtriy"
        

