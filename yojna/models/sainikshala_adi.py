from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class sainikshala_adi(models.Model):
    shikshanik_satra = models.CharField(max_length=10,null=True, blank=True, default=None)
    vidyarthi_name = models.CharField(max_length=80,null=True, blank=True, default=None)
    vadil_name = models.CharField(max_length=80,null=True, blank=True, default=None)
    father_mob = PhoneNumberField(unique=True, blank=True)
    aai_name = models.CharField(max_length=80,null=True, blank=True, default=None)
    aai_mobile = PhoneNumberField(unique=True, blank=True)
    sampurn_patta = models.CharField(max_length=150, null=True, blank=True, default=None)
    tahsil_jilha =  models.CharField(max_length=60, null=True, blank=True, default=None)
    jat_yn = models.CharField(max_length=4, null=True, blank=True, default=None)
    jat_praman = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    birth_num = models.DateField(default=None,null=True,blank=True)
    birth_char = models.CharField(max_length=70, null=True, blank=True, default=None)
    birthplace = models.CharField(max_length=40, null=True, blank=True, default=None)
    nationality = models.CharField(max_length=30, null=True, blank=True, default=None)
    school_name = models.CharField(max_length=70, null=True, blank=True, default=None)
    school_address = models.CharField(max_length=80, null=True, blank=True, default=None)
    medium = models.CharField(max_length=30, null=True, blank=True, default=None)
 
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "sainikshala_adi"
    def __str__(self) -> str:
        return str(self.vidyarthi_name)